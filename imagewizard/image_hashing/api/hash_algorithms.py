import numpy
from PIL import Image
import scipy.fftpack
import pywt
""" Perceptual hashing algorithms in python borrowed from https://github.com/JohannesBuchner/imagehash """

def _binary_array_to_hex(arr):
    """
	internal function to make a hex string out of a binary array.
	"""
    bit_string = ''.join(str(b) for b in 1 * arr.flatten())
    width = int(numpy.ceil(len(bit_string) / 4))
    return '{:0>{width}x}'.format(int(bit_string, 2), width=width)


class ImageHash(object):
    """
	Hash encapsulation. Can be used for dictionary keys and comparisons.
	"""
    def __init__(self, binary_array):
        self.hash = binary_array

    def __str__(self):
        return _binary_array_to_hex(self.hash.flatten())

    def __repr__(self):
        return repr(self.hash)

    def __sub__(self, other):
        if other is None:
            raise TypeError('Other hash must not be None.')
        if self.hash.size != other.hash.size:
            raise TypeError('ImageHashes must be of the same shape.',
                            self.hash.shape, other.hash.shape)
        return numpy.count_nonzero(self.hash.flatten() != other.hash.flatten())

    def __eq__(self, other):
        if other is None:
            return False
        return numpy.array_equal(self.hash.flatten(), other.hash.flatten())

    def __ne__(self, other):
        if other is None:
            return False
        return not numpy.array_equal(self.hash.flatten(), other.hash.flatten())

    def __hash__(self):
        # this returns a 8 bit integer, intentionally shortening the information
        return sum(
            [2**(i % 8) for i, v in enumerate(self.hash.flatten()) if v])


def ahash(image, hash_size=8) -> ImageHash:
    """
	Average Hash computation
    Implementation follows:
    http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html
    Step by step explanation:
    https://www.safaribooksonline.com/blog/2013/11/26/image-hashing-with-python/
    Params:
        image      - must be a PIL instance image or numpy array in RGB or opencv image in BGR
        hash_size  - an integer specifying the hash size, default 8 
    Returns:
        <ImageHash> object. To get the hash value simply use - str(<ImageHash>)
	"""
    if hash_size < 2:
        raise ValueError("Hash size must be greater than or equal to 2")

    # reduce size and complexity, then covert to grayscale
    image = image.convert("L").resize((hash_size, hash_size), Image.ANTIALIAS)

    # find average pixel value; 'pixels' is an array of the pixel values, ranging from 0 (black) to 255 (white)
    pixels = numpy.asarray(image)
    avg = pixels.mean()

    # create string of bits
    diff = pixels > avg
    # make a hash
    return ImageHash(diff)


def dhash(image, hash_size=8):
    """
	Difference Hash computation.
	following http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html
	computes differences horizontally
	Params:
        image      - must be a PIL instance image or numpy array in RGB or opencv image in BGR
        hash_size  - an integer specifying the hash size, default 8
    Returns:
        <ImageHash> object. To get the hash value simply use - str(<ImageHash>)
	"""
    # resize(w, h), but numpy.array((h, w))
    if hash_size < 2:
        raise ValueError("Hash size must be greater than or equal to 2")

    image = image.convert("L").resize((hash_size + 1, hash_size),
                                      Image.ANTIALIAS)
    pixels = numpy.asarray(image)
    # compute differences between columns
    diff = pixels[:, 1:] > pixels[:, :-1]
    return ImageHash(diff)


def dhash_vertical(image, hash_size=8):
    """
	Difference Hash computation.
	following http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html
	computes differences vertically
	Params:
        image      - must be a PIL instance image or numpy array in RGB or opencv image in BGR
        hash_size  - an integer specifying the hash size, default 8 for 64 bit hash
    Returns:
        <ImageHash> object. To get the hash value simply use - str(<ImageHash>)
	"""
    # resize(w, h), but numpy.array((h, w))
    image = image.convert("L").resize((hash_size, hash_size + 1),
                                      Image.ANTIALIAS)
    pixels = numpy.asarray(image)
    # compute differences between rows
    diff = pixels[1:, :] > pixels[:-1, :]
    return ImageHash(diff)


def phash(image, hash_size=8, highfreq_factor=4):
    """
	Perceptual Hash computation.
	Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html
	Params:
        image      - must be a PIL instance image or numpy array in RGB or opencv image in BGR
        hash_size  - an integer specifying the hash size (hash_size * highfreq_factor should be less than number of rows or columns of the gray_image)
        highfreq_factor - an integer specyfing the highfrequency factor
    Returns:
        <ImageHash> object. To get the hash value simply use - str(<ImageHash>)
	"""
    if hash_size < 2:
        raise ValueError("Hash size must be greater than or equal to 2")

    img_size = hash_size * highfreq_factor
    image = image.convert("L").resize((img_size, img_size), Image.ANTIALIAS)
    pixels = numpy.asarray(image)
    dct = scipy.fftpack.dct(scipy.fftpack.dct(pixels, axis=0), axis=1)
    dctlowfreq = dct[:hash_size, :hash_size]
    med = numpy.median(dctlowfreq)
    diff = dctlowfreq > med
    return ImageHash(diff)


def phash_simple(image, hash_size=8, highfreq_factor=4):
    """
	Perceptual Hash computation.
	Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html
	Params:
        image      - must be a PIL instance image or numpy array in RGB or opencv image in BGR
        hash_size  - an integer specifying the hash size (hash_size * highfreq_factor should be less than number of rows or columns of the gray_image)
        highfreq_factor - an integer specyfing the highfrequency factor
    Returns:
        <ImageHash> object. To get the hash value simply use - str(<ImageHash>)
	"""
    img_size = hash_size * highfreq_factor
    image = image.convert("L").resize((img_size, img_size), Image.ANTIALIAS)
    pixels = numpy.asarray(image)
    dct = scipy.fftpack.dct(pixels)
    dctlowfreq = dct[:hash_size, 1:hash_size + 1]
    avg = dctlowfreq.mean()
    diff = dctlowfreq > avg
    return ImageHash(diff)


def whash(image,
          hash_size=8,
          image_scale=None,
          mode='haar',
          remove_max_haar_ll=True):
    """
	Wavelet Hash computation.
	based on https://www.kaggle.com/c/avito-duplicate-ads-detection/
    Params:
        image      - must be a PIL instance image or numpy array in RGB or opencv image in BGR
        hash_size  - must be a power of 2 and less than 'image_scale'
        image_scale- must be power of 2 and less than image size. By default is equal to max power of 2 for an input image.
        mode (see modes in pywt library):
            'haar'  - Haar wavelets, by default
            'db4'   - Daubechies wavelets
        remove_max_haar_ll - remove the lowest low level (LL) frequency using Haar wavelet.
    Returns:
        <ImageHash> object. To get the hash value simply use - str(<ImageHash>)
	"""
    if image_scale is not None:
        assert image_scale & (image_scale -
                              1) == 0, "image_scale is not power of 2"
    else:
        image_natural_scale = 2**int(numpy.log2(min(image.size)))
        image_scale = max(image_natural_scale, hash_size)

    ll_max_level = int(numpy.log2(image_scale))

    level = int(numpy.log2(hash_size))
    assert hash_size & (hash_size - 1) == 0, "hash_size is not power of 2"
    assert level <= ll_max_level, "hash_size in a wrong range"
    dwt_level = ll_max_level - level

    image = image.convert("L").resize((image_scale, image_scale),
                                      Image.ANTIALIAS)
    pixels = numpy.asarray(image) / 255

    # Remove low level frequency LL(max_ll) if @remove_max_haar_ll using haar filter
    if remove_max_haar_ll:
        coeffs = pywt.wavedec2(pixels, 'haar', level=ll_max_level)
        coeffs = list(coeffs)
        coeffs[0] *= 0
        pixels = pywt.waverec2(coeffs, 'haar')

    # Use LL(K) as freq, where K is log2(@hash_size)
    coeffs = pywt.wavedec2(pixels, mode, level=dwt_level)
    dwt_low = coeffs[0]

    # Substract median and compute hash
    med = numpy.median(dwt_low)
    diff = dwt_low > med
    return ImageHash(diff)


# LEGACY CODE
def hex_to_hash(hexstr):
    """
	Convert a stored hash (hex, as retrieved from str(Imagehash))
	back to a Imagehash object.
	Notes:
	1. This algorithm assumes all hashes are bidimensional arrays
	   with dimensions hash_size * hash_size.
	2. This algorithm does not work for hash_size < 2.
	"""
    hash_size = int(numpy.sqrt(len(hexstr) * 4))
    binary_array = '{:0>{width}b}'.format(int(hexstr, 16),
                                          width=hash_size * hash_size)
    bit_rows = [
        binary_array[i:i + hash_size]
        for i in range(0, len(binary_array), hash_size)
    ]
    hash_array = numpy.array([[bool(int(d)) for d in row] for row in bit_rows])
    return ImageHash(hash_array)


def old_hex_to_hash(hexstr, hash_size=8):
    """
	Convert a stored hash (hex, as retrieved from str(Imagehash))
	back to a Imagehash object. This method should be used for
	hashes generated by ImageHash up to version 3.7. For hashes
	generated by newer versions of ImageHash, hex_to_hash should
	be used instead.
	"""
    l = []
    count = hash_size * (hash_size // 4)
    if len(hexstr) != count:
        emsg = 'Expected hex string size of {}.'
        raise ValueError(emsg.format(count))
    for i in range(count // 2):
        h = hexstr[i * 2:i * 2 + 2]
        v = int("0x" + h, 16)
        l.append([v & 2**i > 0 for i in range(8)])
    return ImageHash(numpy.array(l))
