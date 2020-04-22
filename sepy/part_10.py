def search_v2(query_tokens, inverted_index, term_frequency_map, ranking_fn):
    """Given list of tokens from the query, inverted index, term_frequency_map
    and ranking function  return the list of document IDs and score that you think
    should be served as search results.

    Check part_09 to understand signatire of ranking_fn
    Check part_08 to understand the structure of term_frequency_map

    The results should be sorted w.r.t score.

    Result should be a list of tuple
    [
      ("4", 0.98162),
      ("2", 0.97162),
      ("1", 0.0312),
    ]
    1st element -> Document id
    2nd element -> Score
    """
    docs = None
    for token in query_tokens:
        if docs is None:
            docs = inverted_index.get(token, set())
        else:
            docs = docs.intersection(inverted_index.get(token, set()))
    
    return sorted([
      (
        d,
        ranking_fn(query_tokens, d, inverted_index, term_frequency_map),
      )
      for d in docs
    ], key=lambda x: x[1], reverse=True)
