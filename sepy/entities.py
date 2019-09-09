from sepy.part_01 import read_corpus
from sepy.part_02 import cleanse
from sepy.part_03 import get_excerpt
from sepy.part_04 import tokenize
from sepy.part_05 import normalize
from sepy.part_06 import build_inverted_index


class Engine:
    def __init__(self, datasetdir):
        self.datasetdir = datasetdir
        self.documents = []
        self.docmap = {}
        self.index = {}

    def get_stats(self):
        return {
            "count_documents": len(self.documents)
        }

    def read_corpus(self):
        self.documents = read_corpus(self.datasetdir)

    def cleanse(self):
        for doc in self.documents:
            doc["text"] = cleanse(doc["text"])

    def populate_excerpts(self):
        for doc in self.documents:
            doc["excerpt"] = get_excerpt(doc["text"])

    def tokenize(self):
        for doc in self.documents:
            doc["tokens"] = tokenize(doc["text"])

    def normalize(self):
        for doc in self.documents:
            doc["tokens"] = [normalize(t) for t in doc["tokens"]]

    def build_inverted_index(self):
        self.index = build_inverted_index(self.documents)
