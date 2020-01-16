import unittest
import sys
sys.path.append("..")
import imagewizard


class TestSimilarity(unittest.TestCase):

    im_sim = imagewizard.Similarity()
    test_x_hash = ['0x4bd1', 0x4bd1, [0, 1, 1, 0, 1]] 
    test_y_hash = [0x5bd2, 5, [1, 0, 0, 0, 1, 0, 0]]
    
    hamming_result = [3, 8, 5]
    euclidean_result = [1.7320508075688772, 2.8284271247461903, 1.7320508075688772]
    cosine_result = [0.825, 0.25, 0.408]
    manhattan_result = [3, 8, 5]
    jaccard_result = [1.0, 1, 1.0]
    minkowski_result = [1.442, 2.0, 1.442]

    def test_hamming_distance(self):
        for a, b, actual_result in zip(self.test_x_hash, self.test_y_hash, self.hamming_result):
            result = self.im_sim.similarity(a, b, metric='hamming')
            with self.subTest():
                self.assertEqual(result, actual_result, 'input a = {}, b = {}'.format(str(a), str(b)))

    def test_euclidean_distance(self):
        for a, b, actual_result in zip(self.test_x_hash, self.test_y_hash, self.euclidean_result):
            result = self.im_sim.similarity(a, b, metric='euclidean')
            with self.subTest():
                self.assertEqual(result, actual_result, 'input a = {}, b = {}'.format(str(a), str(b)))
    
    def test_cosine_distance(self):
        for a, b, actual_result in zip(self.test_x_hash, self.test_y_hash, self.cosine_result):
            result = self.im_sim.similarity(a, b, metric='cosine')
            with self.subTest():
                self.assertEqual(result, actual_result, 'input a = {}, b = {}'.format(str(a), str(b)))

    def test_manhattan_distance(self):
        for a, b, actual_result in zip(self.test_x_hash, self.test_y_hash, self.manhattan_result):
            result = self.im_sim.similarity(a, b, metric='manhattan')
            with self.subTest():
                self.assertEqual(result, actual_result, 'input a = {}, b = {}'.format(str(a), str(b)))
    
    def test_jaccard_distance(self):
        for a, b, actual_result in zip(self.test_x_hash, self.test_y_hash, self.jaccard_result):
            result = self.im_sim.similarity(a, b, metric='jaccard')
            with self.subTest():
                self.assertEqual(result, actual_result, 'input a = {}, b = {}'.format(str(a), str(b)))
    
    def test_minkowski_distance(self):
        for a, b, actual_result in zip(self.test_x_hash, self.test_y_hash, self.minkowski_result):
            result = self.im_sim.similarity(a, b, metric='minkowski')
            with self.subTest():
                self.assertEqual(result, actual_result, 'input a = {}, b = {}'.format(str(a), str(b)))
