import math


def ranking_fn(query_tokens, doc_id, inverted_index, term_frequency_map):
    """Given inverted index and term frequency index, the
    function should return a score of relevance for the document identified
    with id `doc_id`.

    Check part_08 to understand the structure of term_frequency_map

    The return value should be float.
    """
    return sum(
        [
            term_frequency_map.get(token, {}).get(doc_id, 1) * math.log2(1000/len(inverted_index.get(token, 1)))
            for token in query_tokens
        ]
    )
