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

        results = [
            meterusage_pb2.MeterUsageItem(meterusage=i.meterusage, time=i.time, id=i.id)
            for i in items
        ]
        return meterusage_pb2.MeterUsageResponse(items=results)
