from sepy.part_01 import read_corpus
from sepy.part_02 import cleanse
from sepy.part_03 import get_excerpt
from sepy.part_04 import tokenize
from sepy.part_05 import normalize


class Config:
    def __init__(self, datasetdir):
        self.datasetdir = datasetdir


class Engine:
    def __init__(self, config):
        self.config = config
        self.documents = []
        self.docmap = {}

    def get_stats(self):
        return {
            "count_documents": len(self.documents)
        }

    def read_corpus(self):
        self.documents = read_corpus(self.config.dataset_dir)

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
