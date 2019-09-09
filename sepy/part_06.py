def build_inverted_index(documents):
    """Given a list of documents and return inverted index.

    Documents is a list of document and each document is

    {
      "id": "12312",
      "title": "Some title of a document",
      "body": "a gigantic body of the document",
      "tokens": ["hi", "i", "m", "harry", "potter"],  <-- use this
      "excerpt": "good looking excerpt"
    }

    structure of inverted index

    {
      "word1": set of document ids where word1 exists,
      "word2": set of document ids where word2 exists,
      ...
      ...
      "wordn": set of document ids where wordn exists,
    }
    """
    return {}
