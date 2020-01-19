import unittest
import sys
sys.path.append("..")
import imagewizard
import cv2 as cv
import numpy.testing as npt


class TestProcessing(unittest.TestCase):

    im_pro = imagewizard.Processing()
    street_org = cv.imread("data/original_images/street.png")
    lenna_org = cv.imread("data/original_images/lenna.png")

    # resize tests
    resize_actual = cv.imread(
        "data/processed_images/resize/shrink-300px-300px.png")
    resize_test = im_pro.resize(street_org,
                                resize_width=300,
                                resize_height=300,
                                order='bgr')

    # grayscale tests
    img2grayscale_actual = cv.imread("data/processed_images/gray/gray.png",
                                     cv.IMREAD_GRAYSCALE)
    img2grayscale_test = im_pro.img2grayscale(lenna_org, order='bgr')

    img2grayscale_inv_actual = cv.imread(
        "data/processed_images/gray/gray_inverted.png", cv.IMREAD_GRAYSCALE)
    img2grayscale_inv_test = im_pro.img2grayscale(lenna_org,
                                                  inverted=True,
                                                  order='bgr')

    grayscale_actual = [img2grayscale_actual, img2grayscale_inv_actual]
    grayscale_test = [img2grayscale_test, img2grayscale_inv_test]

    # rotate tests
    rotate_actual = cv.imread("data/processed_images/rotate/rotate-90deg.png")
    rotate_test = im_pro.rotate(lenna_org, rotation_degree = 90, order='bgr')

    # crop tests
    crop_actual = cv.imread("data/processed_images/crop/crop1.png")
    crop_test = im_pro.crop(street_org, start_x = 50, end_x = 100, start_y = 50, end_y = 100, is_percentage = True, order='bgr')

    # mirror tests
    mirror_actual = cv.imread("data/processed_images/mirror/flip_x.png")
    mirror_test = im_pro.mirror(lenna_org, flip_code=1, order='bgr')   

    # blur tests
    blur_actual = cv.imread("data/processed_images/blur/blur5.png")
    blur_test = im_pro.blur(street_org, blur_level = 5, order='bgr')  

    # luminosity tests
    lum_actual = cv.imread("data/processed_images/luminosity/lum_100.png")
    lum_test = im_pro.luminosity(lenna_org, intensity_shift = 100, order = 'bgr') 

    # segmentation tests
    rgb_colors_list = [[224, 166, 147], [110, 34, 71], [195, 98, 100]]
    seg_actual = cv.imread("data/processed_images/segmented_image.png")
    seg_test = im_pro.segmentation(lenna_org, rgb_colors_list, 'bgr') 

    def test_resize(self):
        npt.assert_array_equal(self.resize_test, self.resize_actual, 'Resized image does not equal actual result')

    def test_grayscale(self):
        npt.assert_array_equal(
            self.grayscale_actual, self.grayscale_test,
            'img2grayscale result does not equal actual result')

    def test_rotate(self):
        npt.assert_array_equal(self.rotate_actual, self.rotate_test,
                               'Rotated image does not equal actual result')

    def test_crop(self):
        npt.assert_array_equal(self.crop_actual, self.crop_test,
                               'Cropped image does not equal actual result')

    def test_mirror(self):
        npt.assert_array_equal(self.mirror_actual, self.mirror_test,
                               'Mirrored flip X image does not equal actual result')
    
    def test_blur(self):
        npt.assert_array_equal(self.blur_actual, self.blur_test,
                               'Blurred image does not equal actual result')

    def test_luminosity(self):
        npt.assert_array_equal(self.lum_actual, self.lum_test,
                               'luminosity 100 image does not equal actual result')
    
    def test_segmentation(self):
        npt.assert_array_equal(self.seg_actual, self.seg_test,
                               'segmentation image does not equal actual result')
