import unittest
import sys
sys.path.append("..")
import imagewizard
from PIL import Image
import cv2 as cv


class TestHashing(unittest.TestCase):

    im_hash = imagewizard.Hashing()
    pil_image = Image.open('data/test.png')
    cv2_image = cv.imread('data/test.png')
    test_input = [[pil_image, 'rgb'], [cv2_image, 'bgr']]

    a_hash_result = ['fefff80000000000', 'fefff80000000000']
    a_hash_incorrect_result = ['fefff91000000000', 'feabja1000000000']

    d_hash_result = ['48b09035b16c9ccb', '48b09035b16c9ccb']
    d_hash_incorrect_result = ['48b09035b16c2cba', '48b09035b16c1asb']

    p_hash_result = ['d0ddd594473657c0', 'd0ddd594473657c0']
    p_hash_incorrect_result = ['d0ddd594473354c0', 'd0ddd596543657c0']

    w_hash_result = ['fffffe80101e4420', 'fffffe80101e4420']
    w_hash_incorrect_result = ['ffaaae80101e4420', 'ffaaae80101e4420']

    def test_a_hash(self):
        for input_image, actual_result, incorrect_result in zip(
                self.test_input, self.a_hash_result,
                self.a_hash_incorrect_result):
            result = self.im_hash.ahash(image=input_image[0],
                                        order=input_image[1])
            with self.subTest():
                self.assertEqual(str(result), actual_result,
                                 'output a hash - {}'.format(str(result)))
            with self.subTest():
                self.assertNotEqual(str(result), incorrect_result,
                                    'output a hash - {}'.format(str(result)))

    def test_d_hash(self):
        for input_image, actual_result, incorrect_result in zip(
                self.test_input, self.d_hash_result,
                self.d_hash_incorrect_result):
            result = self.im_hash.dhash(image=input_image[0],
                                        order=input_image[1])
            with self.subTest():
                self.assertEqual(str(result), actual_result,
                                 'output d hash - {}'.format(str(result)))
            with self.subTest():
                self.assertNotEqual(str(result), incorrect_result,
                                    'output a hash - {}'.format(str(result)))

    def test_p_hash(self):
        for input_image, actual_result, incorrect_result in zip(
                self.test_input, self.p_hash_result,
                self.p_hash_incorrect_result):
            result = self.im_hash.phash(image=input_image[0],
                                        order=input_image[1])
            with self.subTest():
                self.assertEqual(str(result), actual_result,
                                 'output p hash - {}'.format(str(result)))
            with self.subTest():
                self.assertNotEqual(str(result), incorrect_result,
                                    'output a hash - {}'.format(str(result)))

    def test_w_hash(self):
        for input_image, actual_result, incorrect_result in zip(
                self.test_input, self.w_hash_result,
                self.w_hash_incorrect_result):
            result = self.im_hash.whash(image=input_image[0],
                                        order=input_image[1])
            with self.subTest():
                self.assertEqual(str(result), actual_result,
                                 'output w hash - {}'.format(str(result)))
            with self.subTest():
                self.assertNotEqual(str(result), incorrect_result,
                                    'output a hash - {}'.format(str(result)))
