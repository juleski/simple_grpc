from __future__ import print_function
import logging

import grpc

from .generated import meterusage_pb2
from .generated import meterusage_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = meterusage_pb2_grpc.MeterUsageServiceStub(channel)
        response = stub.GetMeterUsage(meterusage_pb2.MeterUsageRequest())

    for i in response.items:
        print(i)


if __name__ == "__main__":
    logging.basicConfig()
    run()
