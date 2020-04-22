from collections import defaultdict, Counter


def build_term_frequency(documents):
    """Given list of documents, return term frequency map

    Documents is a list of document and each document is

    {
      "id": "12312",
      "title": "Some title of a document",
      "body": "a gigantic body of the document",
      "tokens": ["hi", "i", "m", "harry", "potter"],  <-- use this
      "excerpt": "good looking excerpt"
    }

    term frequency map looks like this.
    {
      "word1": {
        "doc1": 10,
        "doc2": 5
      }
    }
    """
    tf = defaultdict(dict)
    for doc in documents:
      cmap = Counter(doc["tokens"])
      for token in doc["tokens"]:
        tf[token][doc["id"]] = cmap[token]
    return tf
