import unittest
import sys
sys.path.append("..")
import imagewizard


class TestSimilarity(unittest.TestCase):

    im_sim = imagewizard.Similarity()
    im_pro = imagewizard.Processing()
    im_hash = imagewizard.Hashing()

    test_x_hash = ['0x4bd1', 0x4bd1, [0, 1, 1, 0, 1]] 
    test_y_hash = [0x5bd2, 5, [1, 0, 0, 0, 1, 0, 0]]
    hamming_result = [3, 13, 5]

    def test_hamming_distance(self):
        for a, b, actual_result in zip(self.test_x_hash, self.test_y_hash, self.hamming_result):
            result = self.im_sim.similarity(a, b, metric='hamming')
            with self.subTest():
                self.assertEqual(result, actual_result, 'input a = {}, b = {}'.format(str(a), str(b)))