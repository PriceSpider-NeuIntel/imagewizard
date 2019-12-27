import cv2 as cv
from imagewizard.helpers import img_helpers
""" Class containing the various methods for image processing and transformations. """


class Processing():
    def resize(
            self,
            img_path: str,
            interpolation_method: str = 'shrink',
            resize_width: int = None,
            resize_height: int = None,
            resize_percentage: float = None,
    ) -> cv:
        """ Resize (scale or shrink) image to specified dimensions
            Params:
            img_path: path of the image file to be resized

            interpolation_method: values - s/shrink or z/zoom; default to shrink

            resize_percentage: floating value (0-100) to resize image by the specified percentage
            
            resize_width, resize_height: (in pixels) if unspecified, defaults to 50% of original img width & height. If either only width or height is specified, the other dimension is scale to keep the aspect ratio intact.
            Note: these will be ignored if resize_percentage is specified
            
            Returns: cv2 object
        """
        img = img_helpers.imread(img_path)

        # set the size of image along with interploation methods
        # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC
        # is used for zooming
        if interpolation_method in ['shrink', 's']:
            interpolation = cv.INTER_AREA
        elif interpolation_method in ['zoom', 'z']:
            interpolation = cv.INTER_CUBIC

        # get number of pixel horizontally and vertically
        (height, width) = img.shape[:2]

        # set width and height pixels of transformed image
        if resize_percentage is not None:
            ratio = resize_percentage / 100
            dim = (height * ratio, width * ratio)
        elif resize_width is None and resize_height is not None:
            ratio = resize_height / img.shape[0]
            dim = (int(img.shape[1] * ratio), resize_height)
        elif resize_height is None and resize_width is not None:
            ratio = resize_width / img.shape[1]
            dim = (resize_width, int(img.shape[0] * ratio))
        elif resize_height is not None and resize_width is not None:
            dim = (resize_width, resize_height)
        else:
            dim = (int(width / 2), int(height / 2))

        res_img = cv.resize(img, dim, interpolation=interpolation)
        return res_img

    def img2grayscale(self,
                      img_path: str,
                      to_binary: bool = False,
                      to_zero: bool = False,
                      inverted: bool = False,
                      trunc: bool = False) -> cv:
        """ BGR/RGB to Grayscale conversion
            Params:
            img_path: path of the image file to be resized

            thresholding_options: binary, zero, trunc, inverted binary, inverted zero

            Returns: cv2 object
        """
        img = img_helpers.imread(img_path)

        # convert image to grey scale and return cv2 image object
        gs_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # if thresholding
        if trunc:
            _, gs_img = cv.threshold(gs_img, 127, 255, cv.THRESH_TRUNC)
        elif inverted:
            if to_binary:
                _, gs_img = cv.threshold(gs_img, 120, 255,
                                         cv.THRESH_BINARY_INV)
            elif to_zero:
                _, gs_img = cv.threshold(gs_img, 120, 255,
                                         cv.THRESH_TOZERO_INV)
        else:
            if to_zero:
                _, gs_img = cv.threshold(gs_img, 120, 255, cv.THRESH_TOZERO)
            elif to_binary:
                _, gs_img = cv.threshold(gs_img, 120, 255, cv.THRESH_BINARY)
        return gs_img

    def rotate(self,
               img_path: str,
               rotation_degree: int = 180,
               scaling_factor: float = 1.0) -> cv:
        """ Rotate image by specified degrees anti-clockwise
            Params:
            img_path: path of the image file to be resized

            rotation_degree: rotation angle (in degrees)

            scaling_factor: 1.0 to maintain the original scale of the image. 0.5 to halve the size of the image, to double the size of the image, use 2.0.
        
            Returns: cv2 object
        """
        img = img_helpers.imread(img_path)

        # get the dimensions of the image
        (height, width) = img.shape[:2]

        # calculate the center of the image
        center = (width / 2, height / 2)

        # rotate the image by 180 degrees
        img_matrix = cv.getRotationMatrix2D(center, rotation_degree,
                                            scaling_factor)
        rotated_image = cv.warpAffine(img, img_matrix, (width, height))
        return rotated_image

    def crop(self,
             img_path: str,
             start_x: int,
             end_x: int,
             start_y: int,
             end_y: int,
             is_percentage: bool = False) -> cv:
        """ Crop the image to specified pixel coordinates
            Params:
            img_path: path of the image file to be resized

            start_x: starting pixel coordinate along the x-axis/width of the image

            end_x: ending pixel coordinate along the x-axis/width of the image

            start_y: starting pixle coordinate along the y-axis/height of the image

            end_y: ending pixle coordinate along the y-axis/height of the image

            is_percentage: if True, the coordinates will be considered as percentages

        """
        img = img_helpers.imread(img_path)

        # get the dimensions of the image
        (height, width) = img.shape[:2]

        # compute coordinates if params values are percentages
        if is_percentage:
            start_x, end_x, start_y, end_y = width * (start_x / 100), width * (
                end_x / 100), height * (start_y / 100), height * (end_y / 100)
        cropped_image = img[start_y:end_y, start_x, end_x]
        return cropped_image

    def mirror(self, img_path: str, flip_code: int = 0) -> cv:
        """ Mirror the image
            Params:
            img_path: path of the image file to be resized

            flip_code:  = 0 for flipping the image around the x-axis (vertical flipping);
                        > 0 for flipping around the y-axis (horizontal flipping);
                        < 0 for flipping around both axes
        """
        img = img_helpers.imread(img_path)
        if flip_code in [0, 1, -1]:
            mirrored_image = cv.flip(img, flip_code)
            return mirrored_image
        else:
            raise ValueError("flip code must be 0, 1 or -1")

    def blur(self, img_path: str, kernel_size: int = 5) -> cv:
        """ Averaging blur by convolving the image with a normalized box filter of kernel_size
            Params:
            img_path: path of the image file to be resized

            kernel_size(k): (k X k) normalized box filter for blurring
        """
        img = img_helpers.imread(img_path)
        k = kernel_size
        blur_img = cv.blur(img, (k, k))
        return blur_img
    
    def luminosity(self, img_path, intensity_shift: int) -> cv:
        """ Increase/decrease the brightness of the image
            Params:
            img_path: path of the image file to be resized

            brightness_level: increase brightness level by specified level (0-255)
        """
        img = img_helpers.imread(img_path)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        h, s, v = cv.split(hsv)
        lim = 255 - intensity_shift
        v[v > lim] = 255
        v[v <= lim] += intensity_shift
        final_hsv = cv.merge((h, s, v))
        img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
        return img
