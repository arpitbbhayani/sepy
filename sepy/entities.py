from sepy.part_01 import read_corpus
from sepy.part_02 import cleanse
from sepy.part_03 import get_excerpt
from sepy.part_04 import tokenize
from sepy.part_05 import normalize
from sepy.part_06 import build_inverted_index
from sepy.part_07 import search_v1
from sepy.part_08 import build_term_frequency
from sepy.part_09 import ranking_fn
from sepy.part_10 import search_v2


class Engine:
    def __init__(self, datasetdir):
        self.datasetdir = datasetdir
        self.documents = []
        self.docmap = {}
        self.index = {}
        self.term_frequency = {}

    def get_stats(self):
        return {
            "count_documents": len(self.documents),
            "parts_completed": {
                1: len(self.documents) > 0,
                2: cleanse("Harry Potter") == "harry potter",
                3: bool(len(self.documents) > 0 and self.documents[0].get("excerpt")),
                4: len(tokenize("harry potter")) > 0 and \
                        isinstance(tokenize("harry potter"), (list, tuple, set)),
                5: normalize("houses") == "hous",
                6: len(self.index) > 0,
                7: len(self.search_v1("harry potter")) > 0,
                8: len(self.term_frequency) > 0,
                9: ranking_fn([], "id", {}, {}) != 1,
                10: len(self.search_v1("harry potter")) > 0,
            },
            "total_parts": 10,
        }

    def read_corpus(self):
        self.documents = read_corpus(self.datasetdir)

    def cleanse(self):
        for doc in self.documents:
            doc["text"] = cleanse(doc["text"])

    def populate_excerpts(self):
        for doc in self.documents:
            doc["excerpt"] = get_excerpt(doc["text"])
            self.docmap[doc["id"]] = doc

    def tokenize(self):
        for doc in self.documents:
            doc["tokens"] = tokenize(doc["text"])

    def normalize(self):
        for doc in self.documents:
            doc["tokens"] = [normalize(t) for t in doc["tokens"]]

    def build_inverted_index(self):
        self.index = build_inverted_index(self.documents)

    def build_term_frequency(self):
        self.term_frequency = build_term_frequency(self.documents)

    def get_doc(self, doc_id):
        return self.docmap.get(doc_id)

    def search_v1(self, query):
        query_tokens = [
            normalize(t) for t in tokenize(cleanse(query))
        ]

        doc_ids = search_v1(query_tokens, self.index)[:10]

        return [
            {
                "doc": self.get_doc(doc_id),
                "score": 1
            }
            for doc_id in doc_ids
        ]

    def search_v2(self, query):
        query_tokens = [
            normalize(t) for t in tokenize(cleanse(query))
        ]

        results = search_v2(query_tokens, self.index, self.term_frequency, ranking_fn)[:10]

        return [
            {
                "doc": self.get_doc(doc_id),
                "score": score
            }
            for doc_id, score in results
        ]
