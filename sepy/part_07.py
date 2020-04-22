def search_v1(query_tokens, inverted_index):
    """Given list of tokens from the query and inverted index,
    return the list of document IDs that you think
    should be served as search results.
    """
    s = None
    for token in query_tokens:
        if s is None:
            s = inverted_index.get(token, set())
        else:
            s = s.intersection(inverted_index.get(token, set()))
    return list(s)
