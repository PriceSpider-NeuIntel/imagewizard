from PIL import Image, ImageChops
from imagewizard.helpers import helpers

def trim(image, order: str = 'rgb'):
    """ Trim/Crop an image to its content (removes uniform color spaced padding around the image)
        Params:
            img: (PIL.image)
            order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
        Returns:
            PIL/numpy.array of the order specified
    """
    background = Image.new(image.mode, image.size, image.getpixel((0,0)))
    diff = ImageChops.difference(image, background)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        res = image.crop(bbox)
        if order == 'bgr':
            return helpers.PIL2BGR(res)
        else:
            return res
        