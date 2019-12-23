from imagewizard.similarity_metrics.api.distance_algorithms import Similarity, hex_str_to_int

def similarity_measure(value_src: int, value_query: [int], metric: str ="hamming",) -> [int]:
    """
    The value_src is expected to be an integer or hex or binary or string of hex or binary

    The value_query is expected to be either a simgle value or an array of integers or hex or binary 
    or string of hex or binary.

    The metric argument is the distance measurement metric. The values can be "hamming", "euclidean",
    "manhattan", "nroot", "cosine", "sqroot", "jaccard", "minkowski". The default is hamming.

    The function returns a similarity measure score for the value_src with every value in the 
    value_query.
    
    """
    measures = Similarity()

    # if value_src is hex string -> convert value_src to int
    if isinstance(value_src, str):
        value_src = hex_str_to_int(value_src)

    # converting int to binary array
    value_src = [int(x) for x in list('{0:0b}'.format(value_src))]

    # if value_query is not list, convert value_query to list
    if type(value_query) is not list: value_query = [value_query]

    # if value_query is hex string -> convert value_query to int
    for i, v in enumerate(value_query):
        if isinstance(v, str):
            value_query[i] = hex_str_to_int(v)

    if metric == "hamming":
        # list to track hamming distance between 
        # value_src to every element in value_query
        dist = []

        # get hamming distance
        for val in value_query:
            # converting int to binary array
            val = [int(x) for x in list('{0:0b}'.format(val))]

            dist.append(measures.manhattan_distance(value_src, val))
        
        return dist