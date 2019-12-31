from math import sqrt, pow
from decimal import Decimal
from imagewizard.helpers import hex_str_to_int
"""
Class containing methods to calculate distances between image hashes
Code inspired by https://dataconomy.com/2015/04/implementing-the-five-most-popular-similarity-measures-in-python/
"""

class DistanceAlgorithms():
    """ Five similarity measures function """
    def euclidean_distance(self, _x, _y):
        """ return euclidean distance between two lists """

        return sqrt(sum(pow(a - b, 2) for a, b in zip(_x, _y)))

    def manhattan_distance(self, _x: ([int]), _y: ([int])) -> float:
        """
        return manhattan distance between two lists
        _x, yi Є {0,1} => Hamming distance
        """

        # if _x and _y are not of equal length,
        # the difference should be added as cost to insert or delete the bits
        excess_bits_cost = abs(len(_x) - len(_y))
        return sum(abs(a - b) for a, b in zip(_x, _y)) + excess_bits_cost

    def minkowski_distance(self, _x: ([int]), _y: ([int]), p_value: int = 3) -> float:
        """
        return minkowski distance between two lists
        https://www.gaussianwaves.com/2008/12/distance-hamming-vs-euclidean/
        P=1 => Manhattan Distance
        P=2 => Euclidean distance
        P=1 and xi,yi Є {0,1} => Hamming distance
        w is a weighting factor which is set to ‘1’ when computing Euclidean/Hamming distances
        """

        return float(self.nth_root(
            sum(pow(abs(a - b), p_value) for a, b in zip(_x, _y)), p_value))

    def nth_root(self, value, n_root):
        """ returns the n_root of an value """

        root_value = 1 / float(n_root)
        return round(Decimal(value)**Decimal(root_value), 3)

    def cosine_similarity(self, _x: ([int]), _y:([int])) -> float:
        """ return cosine similarity between two lists """

        numerator = sum(a * b for a, b in zip(_x, _y))
        denominator = self.square_rooted(_x) * self.square_rooted(_y)
        return round(numerator / float(denominator), 3)

    def square_rooted(self, _x):
        """ return 3 rounded square rooted value """

        return round(sqrt(sum([a * a for a in _x])), 3)

    def jaccard_similarity(self, _x: ([int]), _y: ([int])) -> float:
        """ returns the jaccard similarity between two lists """

        intersection_cardinality = len(set.intersection(*[set(_x), set(_y)]))
        union_cardinality = len(set.union(*[set(_x), set(_y)]))
        return intersection_cardinality / float(union_cardinality)


# LEGACY CODE
def hamming_distance(hash_src: int, hash_target: [int]) -> list:
    """ find the hamming distance """

    # if hash_src is hex string -> convert hash_src to int
    if isinstance(hash_src, str):
        hash_src = hex_str_to_int(hash_src)

    # if hash_target is not list, convert hash_target to list
    if type(hash_target) is not list: hash_target = [hash_target]

    # list to track hamming distance between hash_src to every element in hash_target
    num_bits_different_list = []

    # perform XOR on hash_src and hash_target to get hamming distance
    for _hash in hash_target:
        if isinstance(_hash, str):
            _hash = hex_str_to_int(_hash)
        num_bits_different_list.append(bin(hash_src ^ _hash).count('1'))

    return num_bits_different_list
