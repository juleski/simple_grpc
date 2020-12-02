from __future__ import print_function
import logging

import grpc

from ..generated import meterusage_pb2
from ..generated import meterusage_pb2_grpc


def run(page=1, page_size=20):
    response = []
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = meterusage_pb2_grpc.MeterUsageServiceStub(channel)
        response = stub.GetMeterUsage(
            meterusage_pb2.MeterUsageRequest(page=page, page_size=page_size)
        )

        response = [
            {"time": item.time, "meterusage": item.meterusage, "id": item.id}
            for item in response.items
        ]

    return response


if __name__ == "__main__":
    logging.basicConfig()
    results = run()
    for result in results:
        print(result)
