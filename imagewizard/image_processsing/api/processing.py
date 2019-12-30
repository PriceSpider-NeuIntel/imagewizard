from imagewizard.helpers import helpers
from imagewizard.image_processsing.api.colorspaces import colorspaces as ct
from imagewizard.image_processsing.api.geometric_tfs import geometric_tfs as gt
from imagewizard.image_processsing.api.smoothing import smoothing as st
""" Class containing the various methods for image processing and transformations. """


class Processing():
    def imread(self, img_path: str):
        return helpers.imread(img_path)

    def imwrite(self, file_name: str, img):
        return helpers.imwrite(file_name, img)

    def resize(self,
               img,
               interpolation_method: str = 'shrink',
               resize_width: int = None,
               resize_height: int = None,
               resize_percentage: float = None,
               order: str = 'rgb'):
        """ Resize (scale or shrink) image to specified dimensions
            Params:
            img: (numpy.array, PIL.image, cv2.image)

            interpolation_method: (s, z) s/shrink or z/zoom; default to shrink

            resize_percentage: (0, 100) floating value. to resize image by the specified percentage
            
            resize_width, resize_height: (in pixels) if unspecified, defaults to 50% of original img width & height. If either only width or height is specified, the other dimension is scale to keep the aspect ratio intact.
            Note: these will be ignored if resize_percentage is specified

            order: (RGB, BGR) input order of the colors BGR/RGB. Default - order
            Note: The output will be a numpy.array of the same order

            Returns: numpy.array of the order specified
        """
        return gt.resize(img, interpolation_method, resize_width,
                         resize_height, resize_percentage, order)

    def img2grayscale(self,
                      img,
                      to_binary: bool = False,
                      to_zero: bool = False,
                      inverted: bool = False,
                      trunc: bool = False,
                      order: str = 'rgb'):
        """ BGR/RGB to Grayscale conversion
            Params:
            img: (numpy.array, PIL.image, cv2.image)

            thresholding_options: binary, zero, trunc, inverted binary, inverted zero
            
            order: (RGB, BGR) input order of the colors BGR/RGB. Default - order
            Note: The output will be a numpy.array of the same order

            Returns: numpy.array of the order specified
        """
        return ct.img2grayscale(img, to_binary, to_zero, inverted, trunc,
                                order)

    def rotate(self,
               img,
               rotation_degree: int = 180,
               scaling_factor: float = 1.0,
               order: str = 'rgb'):
        """ Rotate image by specified degrees anti-clockwise
            Params:
            img: (numpy.array, PIL.image, cv2.image)

            rotation_degree: rotation angle (in degrees)

            scaling_factor: 1.0 to maintain the original scale of the image. 0.5 to halve the size of the image, to double the size of the image, use 2.0.
        
            order: (RGB, BGR) input order of the colors BGR/RGB. Default - order
            Note: The output will be a numpy.array of the same order

            Returns: numpy.array of the order specified
        """
        return gt.rotate(img, rotation_degree, scaling_factor, order)

    def crop(self,
             img,
             start_x: int,
             end_x: int,
             start_y: int,
             end_y: int,
             is_percentage: bool = False,
             order: str = 'rgb'):
        """ Crop the image to specified pixel coordinates
            Params:
            img: (numpy.array, PIL.image, cv2.image)

            start_x: starting pixel coordinate along the x-axis/width of the image

            end_x: ending pixel coordinate along the x-axis/width of the image

            start_y: starting pixle coordinate along the y-axis/height of the image

            end_y: ending pixle coordinate along the y-axis/height of the image

            is_percentage: if True, the coordinates will be considered as percentages

            order: (RGB, BGR) input order of the colors BGR/RGB. Default - order
            Note: The output will be a numpy.array of the same order

            Returns: numpy.array of the order specified
        """
        return gt.crop(img, start_x, end_x, start_y, end_y, is_percentage,
                       order)

    def mirror(self, img, flip_code: int = 0, order: str = 'rgb'):
        """ Mirror the image
            Params:
            img: (numpy.array, PIL.image, cv2.image)

            flip_code:  = 0 for flipping the image around the x-axis (vertical flipping);
                        > 0 for flipping around the y-axis (horizontal flipping);
                        < 0 for flipping around both axes

            order: (RGB, BGR) input order of the colors BGR/RGB. Default - order
            Note: The output will be a numpy.array of the same order

            Returns: numpy.array of the order specified
        """
        gt.mirror(img, flip_code, order)

    def blur(self, img, kernel_size: int = 5, order: str = 'rgb'):
        """ Averaging blur by convolving the image with a normalized box filter of kernel_size
            Params:
            img: (numpy.array, PIL.image, cv2.image)

            kernel_size(k): (k X k) normalized box filter for blurring
        """
        st.blur(img, kernel_size, order)

    def luminosity(self, img, intensity_shift: int = 20, order: str = 'rgb'):
        """ Increase/decrease the brightness of the image
            Params:
            img: (numpy.array, PIL.image, cv2.image)

            brightness_level: 

            order: (RGB, BGR) input order of the colors BGR/RGB. Default - order
            Note: The output will be a numpy.array of the same order

            Returns: numpy.array of the order specified
        """
        return ct.luminosity(img, intensity_shift, order)