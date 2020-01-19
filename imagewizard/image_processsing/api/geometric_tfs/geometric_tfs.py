""" different geometric transformations like resize, rotation, crop """
import cv2 as cv
from imagewizard.helpers import helpers
import numpy as np


def resize(img,
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
    # img object passed is converted to a BGR array
    # and all the operations are performed. The image will be converted
    # back to specified order and returned as numpy.array
    img = helpers.image2BGR(img, order)

    interpolation_method = 's'
    # set the size of image along with interploation methods
    # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_LINEAR
    # is used for zooming
    if interpolation_method in ['shrink', 's']:
        interpolation = cv.INTER_AREA
    elif interpolation_method in ['zoom', 'z']:
        interpolation = cv.INTER_LINEAR

    # get number of pixel horizontally and vertically
    (height, width) = img.shape[:2]

    # set width and height pixels of transformed image
    if resize_percentage is not None:
        ratio = resize_percentage / 100     
        dim = (int(width * ratio), int(height * ratio))
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
    return helpers.format_output_order_input_BGR(res_img, order)


def rotate(img,
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
    # img object passed is converted to a BGR array
    # and all the operations are performed. The image will be converted
    # back to specified order and returned as numpy.array
    img = helpers.image2BGR(img, order)

    # get the dimensions of the image
    (height, width) = img.shape[:2]

    # calculate the center of the image
    center = (width / 2, height / 2)

    # rotate the image by 180 degrees
    img_matrix = cv.getRotationMatrix2D(center, rotation_degree,
                                        scaling_factor)
    rotated_image = cv.warpAffine(img, img_matrix, (width, height))
    return helpers.format_output_order_input_BGR(rotated_image, order)


def crop(img,
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
            is_percentage: if True, the coordinates will be considered as percentages. Default: False
            order: (RGB, BGR) input order of the colors BGR/RGB. Default: RGB
                Note: The output will be a numpy.array of the same order
        Returns:
            numpy.array of the order specified
    """
    # img object passed is converted to a BGR array
    # and all the operations are performed. The image will be converted
    # back to specified order and returned as numpy.array
    img = helpers.image2BGR(img, order)
    err_msg = ''

    # get the dimensions of the image
    (height, width) = img.shape[:2]

    # compute coordinates if params values are percentages
    if is_percentage:
        if start_x < 0 or start_x > 100:
            err_msg += 'start x: {} out of range 0 - 100. \n'.format(start_x)
        if end_x < 0 or end_x > 100:
            err_msg += 'end x: {} out of range 0 - 100. \n'.format(end_x)
        
        if start_y < 0 or start_y > 100:
            err_msg += 'start y: {} out of range 0 - 100. \n'.format(start_y)
        if end_y < 0 or end_y > 100:
            err_msg += 'end x: {} out of range 0 - 100. \n'.format(end_y)

        if start_x > end_x:
            err_msg += 'start x: {} must be less than end x: {}. \n'.format(start_x, end_x)
        if start_y > end_y:
            err_msg += 'start y: {} must be less than end y: {}. \n'.format(start_y, end_y)

        start_x, end_x, start_y, end_y = width * (start_x / 100), width * (
            end_x / 100), height * (start_y / 100), height * (end_y / 100)
    else:
        if start_x > end_x:
            err_msg += 'start x: {} must be less than end x: {}. \n'.format(start_x, end_x)
        if start_y > end_y:
            err_msg += 'start y: {} must be less than end y: {}. \n'.format(start_y, end_y)
        
        if start_x < 0 or start_x > width:
            err_msg += 'start x: {} is out of range 0 - {}. \n'.format(start_x, width)
        if end_x < 0 or end_x > width:
            err_msg += 'end x: {} is out of range 0 - {}. \n'.format(end_x, width)
        
        if start_y < 0 or start_y > height:
            err_msg += 'start y: {} is out of range 0 - {}. \n'.format(start_y, height)
        if end_y < 0 or end_y > width:
            err_msg += 'end y: {} is out of range 0 - {}. \n'.format(end_y, height)

    if not err_msg == '':
        raise ValueError(err_msg)
    cropped_image = img[int(start_y):int(end_y), int(start_x):int(end_x)]
    return helpers.format_output_order_input_BGR(cropped_image, order)


def mirror(img, flip_code: int, order: str):
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
    # img object passed is converted to a BGR array
    # and all the operations are performed. The image will be converted
    # back to specified order and returned as numpy.array
    img = helpers.image2BGR(img, order)

    if flip_code in [0, 1, -1]:
        mirrored_image = cv.flip(img, flip_code)
        return helpers.format_output_order_input_BGR(mirrored_image, order)
    else:
        raise ValueError("flip code must be 0, 1 or -1")


def skew_affine(img,
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
    # img object passed is converted to a BGR array
    # and all the operations are performed. The image will be converted
    # back to specified order and returned as numpy.array
    img = helpers.image2BGR(img, order)
    rows, cols, _ch = img.shape
    img_matrix = cv.getAffineTransform(input_points, output_points)
    affine_skew_img = cv.warpAffine(img, img_matrix, (cols, rows))
    return helpers.format_output_order_input_BGR(affine_skew_img, order)


def skew_perspective(img,
                     input_points: np.float32,
                     output_points: np.float32,
                     order: str = 'rgb'):
    """ skew image by applying perspective transformation
        Params:
            img: (numpy.array, PIL.image, opencv2.image)
            input_points: four points on input image, ex: np.float32([[56,65],[368,52],[28,387],[389,390]])
            output_points: four points on output location correspoinding to input_points' to be transformed, ex: np.float32([[0,0],[300,0],[0,300],[300,300]])
            order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                Note: The output will be a numpy.array of the same order
        Returns:
            numpy.array of the order specified
    """
    # img object passed is converted to a BGR array
    # and all the operations are performed. The image will be converted
    # back to specified order and returned as numpy.array
    img = helpers.image2BGR(img, order)
    output_cols, output_rows = output_points[3:, :][0][0], output_points[
        3:, :][0][1]
    img_matrix = cv.getPerspectiveTransform(input_points, output_points)
    skew_img = cv.warpPerspective(img, img_matrix, (output_cols, output_rows))
    return skew_img
    # return helpers.format_output_order_input_BGR(skew_img, order)
