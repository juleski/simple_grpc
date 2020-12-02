from google.protobuf.timestamp_pb2 import Timestamp
from ..generated import meterusage_pb2_grpc, meterusage_pb2

from . import session
from .models import MeterUsage


class MeterUsageService(meterusage_pb2_grpc.MeterUsageServiceServicer):
    def GetMeterUsage(self, request, context):
        page = request.page
        page_size = request.page_size
        items = (
            session.query(MeterUsage)
            .limit(page_size)
            .offset((page - 1) * page_size)
            .all()
        )

        results = []
        for i in items:
            timestamp = Timestamp()
            timestamp.FromDatetime(i.time)
            temp = meterusage_pb2.MeterUsageItem(
                meterusage=i.meterusage, time=timestamp, id=i.id
            )
            results.append(temp)

        return meterusage_pb2.MeterUsageResponse(items=results)
