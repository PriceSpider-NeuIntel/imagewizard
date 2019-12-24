from math import sqrt, pow
from decimal import Decimal
from imagewizard.helpers import hex_str_to_int

class Similarity():
    """ Five similarity measures function """
    def euclidean_distance(self, x, y):
        """ return euclidean distance between two lists """

        return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))

    def manhattan_distance(self, x, y):
        """ 
        return manhattan distance between two lists
        x, yi Є {0,1} => Hamming distance 
        """
        # if x and y are not of equal length, the difference should be added as cost to insert or delete the bits
        excess_bits_cost = abs(len(x) - len(y))
        return sum(abs(a - b) for a, b in zip(x, y)) + excess_bits_cost

    def minkowski_distance(self, x, y, p_value):
        """ 
        return minkowski distance between two lists 
        
        https://www.gaussianwaves.com/2008/12/distance-hamming-vs-euclidean/
        P=1 => Manhattan Distance
        P=2 => Euclidean distance
        P=1 and xi,yi Є {0,1} => Hamming distance
        w is a weighting factor which is set to ‘1’ when computing Euclidean/Hamming distances
        """

        return self.nth_root(
            sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)

    def nth_root(self, value, n_root):
        """ returns the n_root of an value """

        root_value = 1 / float(n_root)
        return round(Decimal(value)**Decimal(root_value), 3)

    def cosine_similarity(self, x, y):
        """ return cosine similarity between two lists """

        numerator = sum(a * b for a, b in zip(x, y))
        denominator = self.square_rooted(x) * self.square_rooted(y)
        return round(numerator / float(denominator), 3)

    def square_rooted(self, x):
        """ return 3 rounded square rooted value """

        return round(sqrt(sum([a * a for a in x])), 3)

    def jaccard_similarity(self, x, y):
        """ returns the jaccard similarity between two lists """

        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        return intersection_cardinality / float(union_cardinality)


# LEGACY CODE
def hamming_distance(hash_src: int, hash_target: [int]) -> list:

    # if hash_src is hex string -> convert hash_src to int
    if isinstance(hash_src, str):
        hash_src = hex_str_to_int(hash_src)

    # if hash_target is not list, convert hash_target to list
    if type(hash_target) is not list: hash_target = [hash_target]

    # list to track hamming distance between hash_src to every element in hash_target
    num_bits_different_list = []

    # perform XOR on hash_src and hash_target to get hamming distance
    for hash in hash_target:
        if isinstance(hash, str):
            hash = hex_str_to_int(hash)
        num_bits_different_list.append(bin(hash_src ^ hash).count('1'))

    return num_bits_different_list
