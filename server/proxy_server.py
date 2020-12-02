from flask import Flask, jsonify

app = Flask(__name__)


import grpc

from .generated import meterusage_pb2
from .generated import meterusage_pb2_grpc


@app.route("/meterusage")
def fetch_meterusage():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = meterusage_pb2_grpc.MeterUsageServiceStub(channel)
        response = stub.GetMeterUsage(meterusage_pb2.MeterUsageRequest())

    response = [
        {"time": item.time, "meterusage": item.meterusage} for item in response.items
    ]

    return jsonify(response)
