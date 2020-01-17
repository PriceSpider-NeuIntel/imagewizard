from imagewizard.helpers import helpers
from imagewizard.image_processsing.api.colorspaces import colorspaces as ct
from imagewizard.image_processsing.api.geometric_tfs import geometric_tfs as gt
from imagewizard.image_processsing.api.smoothing import smoothing as st
import numpy as np
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
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                    Note: The output will be a numpy.array of the same order
            Returns:
                numpy.array of the order specified
        """
        return gt.resize(img, interpolation_method, resize_width,
                         resize_height, resize_percentage, order)

    def img2grayscale(self,
                      img,
                      to_binary: bool = False,
                      to_zero: bool = False,
                      inverted: bool = False,
                      trunc: bool = False,
                      is_gray: bool = True,
                      order: str = 'rgb'):
        """ BGR/RGB to Grayscale conversion
            Params:
                img: (numpy.array, PIL.image, cv2.image)
                thresholding_options: binary, zero, trunc, inverted binary, inverted zero
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                    Note: The output will be a numpy.array of the same order
            Returns:
                numpy.array of the order specified
        """
        return ct.img2grayscale(img, to_binary, to_zero, inverted, trunc, is_gray,
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
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                    Note: The output will be a numpy.array of the same order
            Returns:
                numpy.array of the order specified
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
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                    Note: The output will be a numpy.array of the same order
            Returns:
                numpy.array of the order specified
        """
        return gt.crop(img, start_x, end_x, start_y, end_y, is_percentage,
                       order)

    def mirror(self, img, flip_code: int = 0, order: str = 'rgb'):
        """ Mirror the image
            Params:
                img: (numpy.array, PIL.image, cv2.image)
                flip_code:  = 0 for flipping the image around the y-axis (vertical flipping);
                            > 0 for flipping around the x-axis (horizontal flipping);
                            < 0 for flipping around both axes
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                    Note: The output will be a numpy.array of the same order
            Returns:
                numpy.array of the order specified
        """
        return gt.mirror(img, flip_code, order)

    def blur(self, img, blur_level: int = 5, order: str = 'rgb'):
        """ Averaging blur by convolving the image with a normalized box filter of kernel_size
            Params:
                img: (numpy.array, PIL.image, cv2.image)
                blur_level: (int, > 0) intensity of blur
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                    Note: The output will be a numpy.array of the same order
            Returns:
                numpy.array of the order specified
        """
        if blur_level <= 0 or blur_level > 100000:
            raise ValueError('Blur level: {} must be an integer & in the range [1, 100000]'.format(blur_level))
        return st.blur(img, blur_level, order)

    def luminosity(self, img, intensity_shift: int = 20, order: str = 'rgb'):
        """ Increase/decrease the brightness of the image
            Params:
                img: (numpy.array, PIL.image, cv2.image)
                intensity_shift: decrease or increase the brightness level
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                    Note: The output will be a numpy.array of the same order
            Returns:
                numpy.array of the order specified
        """
        return ct.luminosity(img, intensity_shift, order)

    def skew_perspective(self,
                         img,
                         input_points: np.float32,
                         output_points: np.float32,
                         order: str = 'rgb'):
        """ skew image by applying perspective transformation
            Params:
                img: (numpy.array, PIL.image, cv2.image)
                input_points: four points on input image, ex: np.float32([[56,65],[368,52],[28,387],[389,390]])
                output_points: four points on output location correspoinding to input_points' to be transformed, ex: np.float32([[0,0],[300,0],[0,300],[300,300]])
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                    Note: The output will be a numpy.array of the same order
            Returns:
                numpy.array of the order specified
        """
        # TODO: check input_points data type and output_points data type
        return gt.skew_perspective(img, input_points, output_points, order)

    def skew_affine(self,
                    img,
                    input_points: np.float32,
                    output_points: np.float32,
                    order: str = 'rgb'):
        """ skew image by applying affine transformation
            Params:
                img: (numpy.array, PIL.image, cv2.image)
                input_points: three points on input image, ex: np.float32([[50,50],[200,50],[50,200]])
                output_points: three points on output location correspoinding to input_points' to be transformed, np.float32([[10,100],[200,50],[100,250]])
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                    Note: The output will be a numpy.array of the same order
            Returns:
                numpy.array of the order specified
        """
        # TODO: check input_points data type and output_points data type
        return gt.skew_affine(img, input_points, output_points, order)
    
    def segmentation(self, img, rgb_list: [[int]], order: str = 'rgb'):
        """ reconstruct an image with only a specified list of colors
            Params:
                img: (numpy.array, PIL.image, cv2.image)
                rgb_list: 2 dimensional np array with shape (n,3) 3 being the channel values in order RGB, eg: [[224, 166, 147], [110, 34, 71], [195, 98, 100]]
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                    Note: The output will be a numpy.array of the same order
            Returns:
                numpy.array of the order specified
        """
        return ct.image_segmentation(img, rgb_list, order)
