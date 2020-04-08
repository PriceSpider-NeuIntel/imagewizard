import cv2 as cv
import PIL
from PIL import JpegImagePlugin # required for JpegImagePlugin Check below
import numpy as np


###########################################################
# Helper functions for image similarity and hashing methods
###########################################################
def bin_str_to_binary(value: str) -> bin:
    """
    convert a string (binary) to binary string
    '1001' -> '0b1001'
    """
    return bin(int(value, 2))


def hex_str_to_int(value: str) -> int:
    """
    convert a hexadecimal string to integer
    '0x1b1b' -> 6939
    """
    return int(value, 16)


def hex_str_to_hex(value: str) -> hex:
    """
    convert a hexadecimal string to hexadecimal
    '1b1b' -> '0x1b1b'
    """
    return hex(int(value, 16))


def hex_to_bin(value: hex) -> bin:
    """
    convert a hexadecimal to binary
    0xf -> '0b1111'
    """
    return bin(value)


def hash_to_binary_array(value) -> [int]:
    """
    convert a hexadecimal hash to array of binary values padded with 0's to form 64 bit string
    0xf     -> [0..., 1,1,1,1]
    '0xf'   -> [0..., 1,1,1,1]
    """
    if isinstance(value, str):
        # if value is hex string -> convert value to int
        value = hex_str_to_int(value)
    if isinstance(value, list):
        # if value is list of string convert to list of int
        value = list(map(int, value))
    if isinstance(value, int):
        # converting int to binary array
        value = [int(x) for x in list('{0:0b}'.format(value).zfill(64))]
    return value


def format_image_to_PIL(image, order):
    """
    convert an image of type PIL or opencv2 image or numpy array to a PIL image
    """
    if isinstance(image, np.ndarray) and order.lower() in ['bgr', 'rgb']:
        if order.lower() == 'bgr':
            return PIL.Image.fromarray(BGR2RGB(image))
        else:
            return PIL.Image.fromarray(image)
    elif isinstance(image, PIL.JpegImagePlugin.JpegImageFile) or isinstance(
            image, PIL.Image.Image):
        return image
    else:
        raise ValueError(
            'parameter image is not a PIL image, cv2 image or numpy array')


###############################################
# Helper functions for image processing methods
###############################################
def imread(file_name):
    """ read an image given its path/file_name """
    try:
        return cv.imread(file_name)
    except Exception as inst:
        return inst


def imwrite(file_name, img):
    """ write an image object to the disk """
    try:
        return cv.imwrite(file_name, img)
    except Exception as inst:
        return inst


def BGR2RGB(img):
    """
    convert numpy array of the image from BGR to RGB
    note: this method does not realize the channel order (RGB or BGR),
    it simply flips the Red and Blue pixel channel values in the numpy array
    """
    return cv.cvtColor(img, cv.COLOR_BGR2RGB)


def RGB2BGR(img):
    """
    convert numpy array of the image from RGB to BGR
    note: this method does not realize the channel order (RGB or BGR),
    it simply flips the Red and Blue pixel channel values in the numpy array
    """
    return cv.cvtColor(img, cv.COLOR_RGB2BGR)


def PIL2BGR(img):
    """ convert a PIL image object to numpy array of channel order BGR """
    return cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)


def image2BGR(img, order):
    """ convert an image in PIL or cv2 or numpy array to numpy array to a channel order BGR """
    if isinstance(img, np.ndarray):
        if order.lower() == 'rgb':
            img = RGB2BGR(img)
    elif isinstance(img, PIL.JpegImagePlugin.JpegImageFile) or isinstance(
            img, PIL.Image.Image):
        img = PIL2BGR(img)
    else:
        raise ValueError(
            'parameter img is not a PIL image, cv2 image or numpy array')
    return img

def format_output_order_input_RGB(img, order):
    """
    img will be RGB array.
    return the image as numpy.array in the order specified
    defaults to RGB
    """
    if order == 'bgr':
        return RGB2BGR(img)
    return img

def format_output_order_input_BGR(img, order):
    """
    img will be BGR array
    return the image as numpy.array in the order specified
    defaults to RGB
    """
    if order == 'rgb':
        return BGR2RGB(img)
    return img

def calculate_distance(a, b):
    result = np.sqrt(sum((a - b)**2))
    return result
