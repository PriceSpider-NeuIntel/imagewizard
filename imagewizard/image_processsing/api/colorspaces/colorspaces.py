""" change images between different color spaces """
import cv2 as cv
from imagewizard.helpers import helpers


def img2grayscale(img,
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
    # img object passed is converted to a BGR array
    # and all the operations are performed. The image will be converted
    # back to specified order and returned as numpy.array
    img = helpers.image2BGR(img, order)

    # convert image to grey scale
    gs_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # if thresholding
    if trunc:
        _, gs_img = cv.threshold(gs_img, 127, 255, cv.THRESH_TRUNC)
    elif inverted:
        if to_binary:
            _, gs_img = cv.threshold(gs_img, 120, 255, cv.THRESH_BINARY_INV)
        elif to_zero:
            _, gs_img = cv.threshold(gs_img, 120, 255, cv.THRESH_TOZERO_INV)
    else:
        if to_zero:
            _, gs_img = cv.threshold(gs_img, 120, 255, cv.THRESH_TOZERO)
        elif to_binary:
            _, gs_img = cv.threshold(gs_img, 120, 255, cv.THRESH_BINARY)
    return helpers.format_output_image_order(gs_img, order)


def luminosity(img, intensity_shift: int, order: str = 'rgb'):
    """ Increase/decrease the brightness of the image
        Params:
        img: (numpy.array, PIL.image, cv2.image)

        brightness_level: 

        order: (RGB, BGR) input order of the colors BGR/RGB. Default - order
        Note: The output will be a numpy.array of the same order

        Returns: numpy.array of the order specified
    """
    # img object passed is converted to a BGR array
    # and all the operations are performed. The image will be converted
    # back to specified order and returned as numpy.array
    img = helpers.image2BGR(img, order)

    # get the HSV from BGR
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue, sat, brightness_value = cv.split(hsv)

    # prevent overflow of value
    limit = 255 - intensity_shift
    brightness_value[brightness_value > limit] = 255

    # increase the brightness value
    brightness_value[brightness_value <= limit] += intensity_shift

    # re-construct hsv
    final_hsv = cv.merge((hue, sat, brightness_value))

    # convert hsv to BGR and return numpy.array in the order specified
    img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
    return helpers.format_output_image_order(img, order)
