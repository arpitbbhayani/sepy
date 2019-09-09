import argparse
import logging
import coloredlogs

from flask import Flask, jsonify, request
from flask_cors import CORS

from sepy.entities import Config, Stats
from sepy.part_01 import read_corpus


coloredlogs.DEFAULT_LOG_FORMAT = '%(asctime)s:%(levelname)s: %(message)s'
coloredlogs.install(level=logging.INFO)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--datasetdir", help="path to dataset folder")
    args = parser.parse_args()

    config = Config(args.datasetdir)
    stats = Stats()

    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    num_documents = read_corpus(config.datasetdir)
    stats.num_documents = num_documents

    @app.route("/api/status")
    def status():
        return jsonify({
            "health": "ok",
            "stats": stats.__dict__,
        })

    app.run(host="0.0.0.0", port=4000)
