from imagewizard.helpers import helpers
from imagewizard.image_analysis.api.colorspaces import color_analysis as ca
from imagewizard.image_analysis.api.geometrics import trim_to_content as tr
""" Class containing the various methods for image analysis """


class Analysis():
    def mean_color(self, img, order: str = 'rgb'):
        """ Calculates and returns the mean/average color of an image
            Params:
                img: (numpy.array, PIL.image, cv2.image)
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
            Returns:
                Tuple of RGB values of the mean color calculated
        """
        image = helpers.format_image_to_PIL(img, order)
        return ca.mean_color(image)

    def frequent_color(self, img, order: str = 'rgb'):
        """ Calculates and returns the frequent/mode color of an image
            Params:
                img: (numpy.array, PIL.image, cv2.image)
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
            Returns:
                Tuple of RGB values of the mode color calculated
        """
        image = helpers.format_image_to_PIL(img, order)
        return ca.frequent_color(image)

    def dominant_colors(self, img, no_of_colors: int = 3, order: str = 'rgb'):
        """ Return n dominant colors in an image
            Params:
                img: (numpy.array, PIL.image, cv2.image)
                no_of_colors: (int) number of dominant colors (RGB) to return
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
            Returns:
                Array of RGB values correspoinding to dominant colors
        """
        image = helpers.image2BGR(img, order)
        return ca.dominant_colors(image, no_of_colors)

    def trim_to_content(self, img, order: str = 'rgb'):
        """ Trim/Crop an image to its content (removes uniform color spaced padding around the image)
            Params:
                img: (numpy.array, PIL.image, cv2.image)
                order: (RGB, BGR) input order of the colors BGR/RGB. Deafult order: RGB
            Returns:
                numpy.array of the order specified
        """
        image = helpers.format_image_to_PIL(img, order)
        return tr.trim(image, order)
        