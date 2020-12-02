import csv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

engine = create_engine("postgres://postgres:example@localhost:5500/app")
if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define
class MeterUsage(Base):
    __tablename__ = "meter_usages"

    id = Column(Integer, primary_key=True)
    meterusage = Column(Float)
    time = Column(String(100))

    def __repr__(self):
        return f"{self.id}-{self.meterusage}-{self.time}"


MeterUsage.__table__.create(bind=engine, checkfirst=True)

total = session.query(MeterUsage).order_by(None).count()

insert_data = True
if total == 2975:
    insert_data = False
    print("Database already seeded!")


if insert_data:
    # Insert Data
    data = []
    with open("meterusage.csv", "r") as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i == 0:
                i += 1
                continue
            else:
                temp = MeterUsage(meterusage=row[1], time=row[0])
                data.append(temp)
            i += 1

    session.add_all(data)
    session.commit()
    print("Database successfully seeded!")
