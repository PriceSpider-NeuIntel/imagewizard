import unittest
import sys
sys.path.append("..")
import imagewizard


class TestSimilarity(unittest.TestCase):

    test_x = [0x4bd1, 0x4bd1, [0, 1, 1, 0, 1]] 
    test_y = [0x5bd2, 5, [1, 0, 0, 0, 1, 0, 0]]
    result = [3, 13, 5]

    def test_hamming_distance(self):
        for a, b, actual_result in zip(self.test_x, self.test_y, self.result):
            result = imagewizard.similarity(a, b, metric='hamming')
            with self.subTest():
                self.assertEqual(result, actual_result, 'input a = {}, b = {}'.format(str(a), str(b)))