import cv2 as cv
from imagewizard.helpers import helpers

def blur(img, kernel_size: int, order: str):
    """ Averaging blur by convolving the image with a normalized box filter of kernel_size
        Params:
            img: (numpy.array, PIL.image, cv2.image)
            kernel_size(k): (k X k) normalized box filter for blurring
    """
    # img object passed is converted to a BGR array
    # and all the operations are performed. The image will be converted
    # back to specified order and returned as numpy.array
    img = helpers.image2BGR(img, order)

    k = kernel_size
    blur_img = cv.blur(img, (k, k))
    return helpers.format_output_order_input_BGR(blur_img, order)
