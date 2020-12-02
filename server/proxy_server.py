from flask import Flask, jsonify
from flask_cors import cross_origin
from flask import request

from .meterusage.client import run

app = Flask(__name__)


@app.route("/meterusage")
@cross_origin(origins=["http://localhost:*", "http://127.0.0.1:*"])
def fetch_meterusage():
    page = request.args.get("page", 1)
    page_size = request.args.get("page_size", 20)
    response = run(page=int(page), page_size=int(page_size))

    return jsonify(response)
