import os
import sys
import time
import argparse
import logging
import coloredlogs

from flask import Flask, jsonify, request
from flask_cors import CORS

from sepy.entities import Engine
from sepy.entities import cleanse, get_excerpt, tokenize, normalize, ranking_fn, get_query_tokens


coloredlogs.DEFAULT_LOG_FORMAT = '%(asctime)s:%(levelname)s: %(message)s'
coloredlogs.install(level=logging.INFO)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--datasetdir", help="path to dataset folder")
    args = parser.parse_args()

    if not args.datasetdir or not os.path.exists(args.datasetdir):
        print("Please pass the argument --datasetdir with path to your data set folder to start the server.")
        sys.exit(1)

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
        start_time = time.time()
        return jsonify({
            "progress": engine.get_stats(),
            "time": (time.time() - start_time) * 1000
        })

    @app.route("/api/status/1")
    def status_1():
        start_time = time.time()
        return jsonify({
            "documents": engine.get_random_documents(),
            "total_documents": engine.get_total_documents(),
            "time": (time.time() - start_time) * 1000
        })

    @app.route("/api/status/2")
    def status_2():
        start_time = time.time()
        return jsonify({
            "text": cleanse(request.args.get('text') or ''),
            "time": (time.time() - start_time) * 1000
        })

    @app.route("/api/status/3")
    def status_3():
        start_time = time.time()
        return jsonify({
            "text": get_excerpt(request.args.get('text') or ''),
            "time": (time.time() - start_time) * 1000
        })

    @app.route("/api/status/4")
    def status_4():
        start_time = time.time()
        return jsonify({
            "tokens": tokenize(request.args.get('text') or ''),
            "time": (time.time() - start_time) * 1000
        })

    @app.route("/api/status/5")
    def status_5():
        start_time = time.time()
        return jsonify({
            "text": normalize(request.args.get('text') or ''),
            "time": (time.time() - start_time) * 1000
        })

    @app.route("/api/status/6")
    def status_6():
        start_time = time.time()
        return jsonify({
            "documents": [
                engine.get_doc(doc_id)
                for doc_id in (engine.index.get(request.args.get('text')) or [])[:10]
            ],
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

    @app.route("/api/status/8")
    def status_8():
        start_time = time.time()
        word = request.args.get('word') or ''
        doc_freq = engine.term_frequency.get(word) or {}
        term_freqs = [
            {
                "doc_id": k,
                "document": engine.get_doc(k),
                "frequency": v,
            }
            for k, v in doc_freq.items()
        ]
        return jsonify({
            "frequencies": term_freqs[:25],
            "time": (time.time() - start_time) * 1000
        })

    @app.route("/api/status/9")
    def status_9():
        start_time = time.time()
        query = request.args.get('q') or ''
        doc_id = request.args.get('doc_id')
        return jsonify({
            "score": ranking_fn(get_query_tokens(query), doc_id,
                                engine.index, engine.term_frequency),
            "time": (time.time() - start_time) * 1000
        })

    @app.route("/api/search_v2")
    def search_v2():
        start_time = time.time()
        documents = engine.search_v2(request.args.get('q'))
        return jsonify({
            "documents": documents,
            "time": (time.time() - start_time) * 1000
        })

    @app.route("/api/docs/<doc_id>")
    def get_doc(doc_id):
        start_time = time.time()
        document = engine.get_doc(doc_id)
        return jsonify({
            "document": document,
            "time": (time.time() - start_time) * 1000
        })

    app.run(host="0.0.0.0", port=4000)
