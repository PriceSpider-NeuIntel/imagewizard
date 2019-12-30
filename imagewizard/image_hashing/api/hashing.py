import os.path
from imagewizard.image_hashing.api.hash_algorithms import ahash, dhash_vertical, dhash, phash, phash_simple, whash
from imagewizard.helpers import helpers

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       'VERSION')) as fi:
    __version__ = fi.read().strip()
""" Class containing method to perform various hashing on image """

class Hashing():
    def ahash(self, image, hash_size: int = 8, order: str = 'rgb'):
        """
		Average Hash computation
		Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html
		Step by step explanation:
        https://www.safaribooksonline.com/blog/2013/11/26/image-hashing-with-python/

		@image must be a PIL instance image or numpy array RGB.
		"""
        image = helpers.format_image_for_hashing(image, order)
        return ahash(image, hash_size)

    def dhash(self, image, hash_size=8, order: str = 'rgb'):
        """
		Difference Hash computation.
		following http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html
		computes differences horizontally

		@image must be a PIL instance image or numpy array RGB.
		"""
        image = helpers.format_image_for_hashing(image, order)
        return dhash(image, hash_size)

    def dhash_vertical(self, image, hash_size=8, order: str = 'rgb'):
        """
		Difference Hash computation.
		following http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html
		computes differences vertically

		@image must be a PIL instance image or numpy array RGB.
		"""
        image = helpers.format_image_for_hashing(image, order)
        return dhash_vertical(image, hash_size)

    def phash(self, image, hash_size=8, highfreq_factor=4, order: str = 'rgb'):
        """
		Perceptual Hash computation.
		Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

		@image must be a PIL instance image or numpy array RGB.
		"""
        image = helpers.format_image_for_hashing(image, order)
        return phash(image, hash_size, highfreq_factor)

    def phash_simple(self, image, hash_size=8, highfreq_factor=4, order: str = 'rgb'):
        """
		Perceptual Hash computation.
		Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

		@image must be a PIL instance image or numpy array RGB.
		"""
        image = helpers.format_image_for_hashing(image, order)
        return phash_simple(image, hash_size, highfreq_factor)

    def whash(self,
              image,
              hash_size=8,
              image_scale=None,
              mode='haar',
              remove_max_haar_ll=True,
			  order: str = 'rgb'):
        """
		Wavelet Hash computation.

		based on https://www.kaggle.com/c/avito-duplicate-ads-detection/

		@image must be a PIL instance image or numpy array RGB.
		@hash_size must be a power of 2 and less than @image_scale.
		@image_scale must be power of 2 and less than image size. By default is equal to max
			power of 2 for an input image.
		@mode (see modes in pywt library):
			'haar' - Haar wavelets, by default
			'db4' - Daubechies wavelets
		@remove_max_haar_ll - remove the lowest low level (LL) frequency using Haar wavelet.
		"""
        image = helpers.format_image_for_hashing(image, order)
        return whash(image, hash_size, image_scale, mode, remove_max_haar_ll)
