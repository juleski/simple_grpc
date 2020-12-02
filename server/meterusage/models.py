from . import Base, engine
from sqlalchemy import Column, Integer, String, Float, DateTime


class MeterUsage(Base):
    __tablename__ = "meter_usages"

    id = Column(Integer, primary_key=True)
    meterusage = Column(Float)
    time = Column(DateTime)

    def __repr__(self):
        return f"{self.id}-{self.meterusage}-{self.time}"


MeterUsage.__table__.create(bind=engine, checkfirst=True)
