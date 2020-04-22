import os
import json


def read_corpus(dataset_dir):
    """Given a valid folder path in `dataset_dir`, read all files
    present in folder (even nested within sub-folders)
    and return the "documents" for the engine.

    input: path of the dataset folder.
    output: list of documents

    each document is of the form
    {
      "id": "12312",
      "title": "Some title of a document",
      "body": "a gigantic body of the document"
    }
    """
    docs = []
    for (a, b, c) in os.walk(dataset_dir):
      for f in c:
        if not f.endswith('.json'):
          continue
        with open(os.path.join(a, f)) as fp:
          data = json.loads(fp.read())
          docs.append({
            "id": data["documentId"],
            "title": data["title"],
            "body": data["text"],
          })
    return docs
