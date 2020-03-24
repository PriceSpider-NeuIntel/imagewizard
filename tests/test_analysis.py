import unittest
import sys
sys.path.append("..")
import imagewizard
import cv2 as cv
import numpy.testing as npt
import numpy as np


class TestAnalysis(unittest.TestCase):

    im_analysis = imagewizard.Analysis()
    lenna_org = cv.imread("data/original_images/lenna.png")
    quiet_flow_org = cv.imread("data/original_images/quiet_flow10.png")

    # mean color test
    mean_actual = (180, 99, 105)
    mean_test = im_analysis.mean_color(lenna_org, 'bgr')

    # mode color test
    mode_actual = (88, 18, 60)
    mode_test = im_analysis.frequent_color(lenna_org, 'bgr')

    # trim to content test
    trim_actual = cv.imread("data/analysed_images/crop_to_content/trimmed_quite_flow10.png")
    trim_test = im_analysis.trim_to_content(quiet_flow_org, 'bgr')

    # dominant color test
    dominant_actual = np.asarray([[223, 163, 144], [108,  33,  71], [193,  95,  99]])
    dominant_test = im_analysis.dominant_colors(lenna_org, 3, 'bgr')

    def test_mean(self):
        npt.assert_array_equal(self.mean_actual, self.mean_test, 'mean/average color does not equal actual result')
    
    def test_mode(self):
        npt.assert_array_equal(self.mode_actual, self.mode_test, 'mode/frequent color does not equal actual result')

    def test_trim(self):
        npt.assert_array_equal(self.trim_actual, self.trim_test, 'trimmed test image does not equal actual result')

    def test_dominant(self):
        npt.assert_array_equal(self.dominant_actual, self.dominant_test, 'dominant colors does not equal actual result')
