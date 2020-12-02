from flask import Flask, jsonify, make_response
from flask_cors import cross_origin
from flask import request

from .meterusage.client import run

app = Flask(__name__)


@app.route("/meterusage")
@cross_origin()
def fetch_meterusage():
    page = request.args.get("page", 1)
    page_size = request.args.get("page_size", 20)
    try:
        response = run(page=int(page), page_size=int(page_size))
    except ValueError:
        error_message = jsonify(
            {
                "error": "Invalid Query Parameters. Please check page and page_size passed"
            }
        )
        return make_response(error_message, 404)

    return jsonify(response)
