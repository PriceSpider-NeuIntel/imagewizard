from imagewizard.similarity_metrics.api.distance_algorithms import Similarity, hex_str_to_int


def format_value_to_binary_array(value) -> ([int]):
    if isinstance(value, str):
        # if value is hex string -> convert value to int
        value = hex_str_to_int(value)
    if isinstance(value, list):
        # if value is list of string convert to list of int
        value = list(map(int, value))
    if isinstance(value, int):
        # converting int to binary array
        value = [int(x) for x in list('{0:0b}'.format(value))]
    return (value)


def similarity(
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
    measures = Similarity()
    value_src, value_query = format_value_to_binary_array(
        value_src), format_value_to_binary_array(value_query)

    if metric == 'hamming' or metric == 'manhattan':
        return measures.manhattan_distance(value_src, value_query)
    
    if metric == 'cosine':
        return measures.cosine_similarity(value_src, value_query)

    if metric == 'euclidean':
        return measures.euclidean_distance(value_src, value_query)

    if metric == 'jaccard':
        return measures.jaccard_similarity(value_src, value_query)
    
    if metric == 'minkowski' or metric =='min':
        return measures.minkowski_distance(value_src, value_query)
    
    else:
        raise ValueError("Invalid value '{}' for argument metric".format(metric))