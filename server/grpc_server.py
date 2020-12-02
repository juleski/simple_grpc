from concurrent import futures
import grpc

from .generated import meterusage_pb2_grpc
from .meterusage.service import MeterUsageService


class Server:
    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        meterusage_pb2_grpc.add_MeterUsageServiceServicer_to_server(
            MeterUsageService(), server
        )
        server.add_insecure_port("[::]:50051")
        server.start()
        server.wait_for_termination()


if __name__ == "__main__":
    Server.run()
