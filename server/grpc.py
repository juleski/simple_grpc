from .generated import meterusage_pb2_grpc, meterusage_pb2
from .service.data import get_csv_data


class MeterUsage(meterusage_pb2_grpc.MeterUsageServiceServicer):
    def GetMeterUsage(self, requext, context):
        csv_data = [meterusage_pb2.MeterUsageItem(**item) for item in get_csv_data()]
        return meterusage_pb2.MeterUsageResponse(items=csv_data)
