import time
import argparse
import logging
import coloredlogs

from flask import Flask, jsonify, request
from flask_cors import CORS

from sepy.entities import Engine


coloredlogs.DEFAULT_LOG_FORMAT = '%(asctime)s:%(levelname)s: %(message)s'
coloredlogs.install(level=logging.INFO)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--datasetdir", help="path to dataset folder")
    args = parser.parse_args()

    engine = Engine(args.datasetdir)

    engine.read_corpus()
    engine.cleanse()
    engine.populate_excerpts()
    engine.tokenize()
    engine.normalize()
    engine.build_inverted_index()
    engine.build_term_frequency()

    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})

    @app.route("/api/status")
    def status():
        return jsonify({
            "progress": engine.get_stats(),
        })

    @app.route("/api/docs/<doc_id>")
    def get_doc(doc_id):
        start_time = time.time()
        document = engine.get_doc(doc_id)
        return jsonify({
            "document": document,
            "time": (time.time() - start_time) * 1000
        })

    @app.route("/api/search_v1")
    def search_v1():
        start_time = time.time()
        documents = engine.search_v1(request.args.get('q'))
        return jsonify({
            "documents": documents,
            "time": (time.time() - start_time) * 1000
        })

    app.run(host="0.0.0.0", port=4000)
