from imagewizard.image_hash_similarity.api.distance_algorithms import DistanceAlgorithms
from imagewizard.helpers.helpers import hash_to_binary_array
from imagewizard.image_hashing.api.hash_algorithms import ImageHash
""" Class containing method to calculate various distances between image hashes """

class Similarity():
    def similarity(
            self,
            value_src: [int],
            value_query: [int],
            metric: str = "hamming",
    ) -> int:
        """
        Params:
            value_src, value_query: must be an integer or hexadecimal or array of binary or array of ints
            metrics: "hamming", "euclidean", "manhattan", "cosine", "jaccard", "minkowski". The metric argument is the distance measurement metric. Defaults to hamming.
        Returns:
            similarity measure score
        """
        measures = DistanceAlgorithms()

        # if hash values are of type ImageHash, convert to str
        value_src = str(value_src) if isinstance(value_src, ImageHash) else value_src
        value_query = str(value_query) if isinstance(value_query, ImageHash) else value_query

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
