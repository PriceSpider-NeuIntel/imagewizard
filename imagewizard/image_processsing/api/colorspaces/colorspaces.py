""" change images between different color spaces """
import cv2 as cv
import numpy as np
from imagewizard.helpers import helpers


def img2grayscale(img,
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
    # img object passed is converted to a BGR array
    # and all the operations are performed. The image will be converted
    # back to specified order and returned as numpy.array
    img = helpers.image2BGR(img, order)

    # convert image to grey scale
    if is_gray:
        gs_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # if thresholding/inverting
        if inverted:
            if trunc:
                _, gs_img = cv.threshold(gs_img, 127, 255, cv.THRESH_TRUNC)
                gs_img = cv.bitwise_not(gs_img)
            elif to_binary:
                _, gs_img = cv.threshold(gs_img, 120, 255,
                                         cv.THRESH_BINARY_INV)
            elif to_zero:
                _, gs_img = cv.threshold(gs_img, 120, 255,
                                         cv.THRESH_TOZERO_INV)
            else:
                gs_img = cv.bitwise_not(gs_img)
        else:
            if trunc:
                _, gs_img = cv.threshold(gs_img, 127, 255, cv.THRESH_TRUNC)
            elif to_binary:
                _, gs_img = cv.threshold(gs_img, 120, 255, cv.THRESH_BINARY)
            elif to_zero:
                _, gs_img = cv.threshold(gs_img, 120, 255, cv.THRESH_TOZERO)
    else:
        gs_img = img
        if inverted:
            gs_img = cv.bitwise_not(gs_img)

    return helpers.format_output_order_input_BGR(gs_img, order)


def luminosity(img, intensity_shift: int, order: str = 'rgb'):
    """ Increase/decrease the brightness of the image
        Params:
            img: (numpy.array, PIL.image, cv2.image)
            intensity_shift: decrease or increase the brightness level
            order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                Note: The output will be a numpy.array of the same order
        Returns:
            numpy.array of the order specified
    """
    # img object passed is converted to a BGR array
    # and all the operations are performed. The image will be converted
    # back to specified order and returned as numpy.array
    img = helpers.image2BGR(img, order)

    # get the HSV from BGR
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue, sat, brightness_value = cv.split(hsv)

    # brighten the pixels (intensity_shift > 0)
    if intensity_shift > 0:
        # prevent overflow of value
        limit = 255 - intensity_shift
        brightness_value[brightness_value > limit] = 255

        # increase the brightness value
        brightness_value[brightness_value <= limit] += intensity_shift

    # darken the pixels (intensity_shift < 0)
    else:
        # prevent overflow of value
        limit = -(intensity_shift)
        brightness_value[brightness_value < limit] = 0

        # decrease the brightness value
        brightness_value[brightness_value >= limit] -= limit

    # re-construct hsv
    final_hsv = cv.merge((hue, sat, brightness_value))

    # convert hsv to BGR and return numpy.array in the order specified
    img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
    return helpers.format_output_order_input_BGR(img, order)


def image_segmentation(image, rgb_list, order: str = 'rgb'):
    """ reconstruct an image with only a specified list of colors
        Params:
            img: (numpy.array, PIL.image, cv2.image)
            rgb_list: colors list - a 2 dimensional np array with shape (n,3) 3 being the channel values in order RGB, eg: [[224, 166, 147], [110, 34, 71], [195, 98, 100]]
            order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
                Note: The output will be a numpy.array of the same order
        Returns:
            numpy.array of the order specified
    """
    image = helpers.format_image_to_PIL(image, order)

    # create an array of pixel values from the given image
    pixels = np.array(image.getdata(), dtype=np.uint8)

    # convert rgb_list to a numpy array
    rgb_list = np.array(rgb_list)
    rgb_list = np.array([rgb_list]) if rgb_list.ndim == 1 else rgb_list
    if not rgb_list.ndim == 2 or not rgb_list.shape[1] == 3:
        raise ValueError(
            'rgb_list must be a two dimensional array of shape (n, 3)')

    # create an array of empty pixel values
    new_pixels = [None] * len(image.getdata())

    # assign new pixel the color closest to the original image's pixel value
    for idx, pixel in enumerate(pixels):
        shortest = float('Inf')
        for color in rgb_list:
            distance = helpers.calculate_distance(color, pixel)
            if distance < shortest:
                shortest = distance
                nearest = color
        new_pixels[idx] = nearest
    _w, _h = image.size

    # reconstruct the image np array with the new pixels
    new_pixels = np.asarray(new_pixels)\
        .astype('uint8')\
        .reshape((_h, _w, 3))
    return helpers.format_output_order_input_RGB(new_pixels, order)
