from imagewizard.helpers import helpers
from .kmeans_colors import Kmeans


def frequent_color(image):
    """ Calculates and returns the frequent/mode color of an image
        Params:
            image: (numpy.array, PIL.image, cv2.image)
        Returns:
            Tuple of RGB values
    """
    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    return most_frequent_pixel[1]


def mean_color(img):
    """ Calculates and returns the mean/average color of an image
        Params:
            img: (numpy.array, PIL.image, cv2.image)
        Returns:
            Tuple of RGB values 
    """
    colour_tuple = [None, None, None]
    for channel in range(3):

        # Get data for one channel at a time
        pixels = img.getdata(band=channel)
        values = []
        for pixel in pixels:
            values.append(pixel)
        colour_tuple[channel] = int(sum(values) / len(values))

    return tuple(colour_tuple)

def dominant_colors(image, no_of_colors: int = 3):
    """ Return n dominant colors in an image
        Params:
            image: (PIL.image)
            no_of_colors: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
        Returns:
            Array of tuples of RGB values correspoinding to dominant colors
    """
    k = Kmeans()
    k.k = no_of_colors
    res = k.run(image)
    dominant_rgb_list = [list(map(int, tup)) for tup in res]
    return dominant_rgb_list
