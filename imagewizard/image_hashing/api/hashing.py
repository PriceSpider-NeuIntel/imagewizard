import os.path
from imagewizard.image_hashing.api.hash_algorithms import ahash, dhash_vertical, dhash, phash, phash_simple, whash
from imagewizard.helpers import helpers
""" Class containing method to perform various hashing on image """


class Hashing():
    def ahash(self, image, hash_size: int = 8, order: str = 'rgb'):
        """
        Average Hash computation
        Params:
            image      - must be a PIL instance image or numpy array in RGB or opencv image in BGR
            hash_size  - (integer) default 8 for 64 bit hash
            order      - (string) RGB, BGR: input order of the colors BGR/RGB. Deafult order: RGB
        Returns:
            <ImageHash> object. To get the hash value simply use - str(<ImageHash>)
        """
        image = helpers.format_image_to_PIL(image, order)
        return ahash(image, hash_size)

    def dhash(self, image, hash_size=8, order: str = 'rgb'):
        """
        Difference Hash computation.
        Params:
            image      - must be a PIL instance image or numpy array in RGB or opencv image in BGR
            hash_size  - (integer) default 8 for 64 bit hash
            order      - (string) RGB, BGR: input order of the colors BGR/RGB. Deafult order: RGB
        Returns:
            <ImageHash> object. To get the hash value simply use - str(<ImageHash>)
        """
        image = helpers.format_image_to_PIL(image, order)
        return dhash(image, hash_size)

    def dhash_vertical(self, image, hash_size=8, order: str = 'rgb'):
        """
        Difference Hash computation.
        Params:
            image      - must be a PIL instance image or numpy array in RGB or opencv image in BGR
            hash_size  - (integer) default 8 for 64 bit hash
            order      - (string) RGB, BGR: input order of the colors BGR/RGB. Deafult order: RGB
        Returns:
            <ImageHash> object. To get the hash value simply use - str(<ImageHash>)
        """
        image = helpers.format_image_to_PIL(image, order)
        return dhash_vertical(image, hash_size)

    def phash(self, image, hash_size=8, highfreq_factor=4, order: str = 'rgb'):
        """
        Perceptual Hash computation.
        Params:
            image      - must be a PIL instance image or numpy array in RGB or opencv image in BGR
            hash_size  - an integer specifying the hash size (hash_size * highfreq_factor should be less than number of rows or columns of the gray_image)
            highfreq_factor - an integer specyfing the highfrequency factor
        Returns:
            <ImageHash> object. To get the hash value simply use - str(<ImageHash>)
        """
        image = helpers.format_image_to_PIL(image, order)
        return phash(image, hash_size, highfreq_factor)

    def phash_simple(self,
                     image,
                     hash_size=8,
                     highfreq_factor=4,
                     order: str = 'rgb'):
        """
        Perceptual Hash computation.
    	Params:
            image      - must be a PIL instance image or numpy array in RGB or opencv image in BGR
            hash_size  - an integer specifying the hash size (hash_size * highfreq_factor should be less than number of rows or columns of the gray_image)
            highfreq_factor - an integer specyfing the highfrequency factor
        Returns:
            <ImageHash> object. To get the hash value simply use - str(<ImageHash>)
        """
        image = helpers.format_image_to_PIL(image, order)
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
        image = helpers.format_image_to_PIL(image, order)
        return whash(image, hash_size, image_scale, mode, remove_max_haar_ll)
