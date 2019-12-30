import cv2 as cv
import PIL
import numpy as np


###########################################################
# Helper functions for image similarity and hashing methods
###########################################################
def bin_str_to_binary(value: str) -> bin:
    return bin(int(value, 2))


def hex_str_to_int(value: str) -> int:
    return int(value, 16)


def hex_str_to_hex(value: str) -> hex:
    return hex(int(value, 16))


def hex_to_bin(value: hex) -> bin:
    return bin(value)


def hash_to_binary_array(value) -> ([int]):
    if isinstance(value, str):
        # if value is hex string -> convert value to int
        value = hex_str_to_int(value)
    if isinstance(value, list):
        # if value is list of string convert to list of int
        value = list(map(int, value))
    if isinstance(value, int):
        # converting int to binary array
        value = [int(x) for x in list('{0:0b}'.format(value))]
    return (value)


###############################################
# Helper functions for image processing methods
###############################################
def imread(file_name):
    try:
        return cv.imread(file_name)
    except Exception as inst:
        return inst


def imwrite(file_name, img):
    try:
        return cv.imwrite(file_name, img)
    except Exception as inst:
        return inst


def BGR2RGB(img):
    return cv.cvtColor(img, cv.COLOR_BGR2RGB)


def RGB2BGR(img):
    return cv.cvtColor(img, cv.COLOR_RGB2BGR)


def PIL2BGR(img):
    return cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)


def image2BGR(img, order):
    if isinstance(img, np.ndarray):
        if order.lower() == 'rgb':
            img = RGB2BGR(img)
    elif isinstance(img, PIL.JpegImagePlugin.JpegImageFile):
        img = PIL2BGR(img)
    else:
        raise ValueError(
            'parameter img is not a PIL image, cv2 image or numpy array')
    return img


def format_output_image_order(img, order):
    # img will be BGR array
    # return the image as numpy.array in the order specified
    # defaults to RGB
    if order == 'rgb':
        return BGR2RGB(img)
    return img
