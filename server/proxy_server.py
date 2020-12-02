from flask import Flask, jsonify
from flask_cors import cross_origin

app = Flask(__name__)


import grpc

from .generated import meterusage_pb2
from .generated import meterusage_pb2_grpc


@app.route("/meterusage")
@cross_origin(origins=["localhost:*", "http://127.0.0.1:*"])
def fetch_meterusage():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = meterusage_pb2_grpc.MeterUsageServiceStub(channel)
        response = stub.GetMeterUsage(meterusage_pb2.MeterUsageRequest())

    response = [
        {"time": item.time, "meterusage": item.meterusage} for item in response.items
    ]

    return jsonify(response)
