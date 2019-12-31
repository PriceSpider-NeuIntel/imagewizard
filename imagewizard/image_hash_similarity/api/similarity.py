from imagewizard.image_hash_similarity.api.distance_algorithms import DistanceAlgorithms
from imagewizard.helpers.helpers import hash_to_binary_array
""" Class containing method to calculate various distances between image hashes """

class Similarity():
    def similarity(
            self,
            value_src: [int],
            value_query: [int],
            metric: str = "hamming",
    ) -> int:
        """
        The value_src and value_query is expected to be an integer or hexadecimal or array of binary
        or array of ints

        The metric argument is the distance measurement metric. The values can be "hamming", "euclidean",
        "manhattan", "cosine", "jaccard", "minkowski". The default is hamming.

        The function returns a similarity measure score for the value_src with every value in the
        value_query.
        
        """
        measures = DistanceAlgorithms()
        value_src, value_query = hash_to_binary_array(
            value_src), hash_to_binary_array(value_query)

        if metric == 'hamming' or metric == 'manhattan':
            return measures.manhattan_distance(value_src, value_query)

        if metric == 'cosine':
            return measures.cosine_similarity(value_src, value_query)

        if metric == 'euclidean':
            return measures.euclidean_distance(value_src, value_query)

        if metric == 'jaccard':
            return measures.jaccard_similarity(value_src, value_query)

        if metric == 'minkowski' or metric == 'min':
            return measures.minkowski_distance(value_src, value_query)

        else:
            raise ValueError(
                "Invalid value '{}' for argument 'metric'".format(metric))
