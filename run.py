import argparse
import logging
import coloredlogs

from flask import Flask, jsonify
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

    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.route("/api/status")
    def status():
        return jsonify({
            "health": "ok",
            "stats": engine.get_stats(),
        })

    app.run(host="0.0.0.0", port=4000)
