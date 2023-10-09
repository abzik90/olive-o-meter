import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an SQLite database (you can change the database URL as needed)
database_url = 'sqlite:///olive_readings.db'
engine = db.create_engine(database_url)

# Create a SQLAlchemy session
Session = sessionmaker(bind=engine)
session = Session()

# Create a declarative base class for defining the table
Base = declarative_base()

# Define the OliveReadings table class
class OliveReadings(Base):
    __tablename__ = 'OliveReadings'

    id = db.Column(db.Integer, primary_key=True)
    sampleTime = db.Column(db.String)
    nm_525_ON = db.Column(db.Integer)
    nm_525_OFF = db.Column(db.Integer)
    nm_680_ON = db.Column(db.Integer)
    nm_680_OFF = db.Column(db.Integer)
    nm_740_ON = db.Column(db.Integer)
    nm_740_OFF = db.Column(db.Integer)
    nm_980_ON = db.Column(db.Integer)
    nm_980_OFF = db.Column(db.Integer)
    nm_1450_ON = db.Column(db.Integer)
    nm_1450_OFF = db.Column(db.Integer)

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Define a class for interacting with the OliveReadings table
class OliveReadingsManager:
    def createReading(self, sample_time, nm_525_ON, nm_525_OFF, nm_680_ON, nm_680_OFF,
                       nm_740_ON, nm_740_OFF, nm_980_ON, nm_980_OFF, nm_1450_ON, nm_1450_OFF):
        new_reading = OliveReadings(
            sampleTime=sample_time,
            nm_525_ON=nm_525_ON,
            nm_525_OFF=nm_525_OFF,
            nm_680_ON=nm_680_ON,
            nm_680_OFF=nm_680_OFF,
            nm_740_ON=nm_740_ON,
            nm_740_OFF=nm_740_OFF,
            nm_980_ON=nm_980_ON,
            nm_980_OFF=nm_980_OFF,
            nm_1450_ON=nm_1450_ON,
            nm_1450_OFF=nm_1450_OFF
        )
        session.add(new_reading)
        session.commit()

    def getReadings(self):
        return session.query(OliveReadings).all()
    def getLastReadingId(self):
        return session.query(OliveReadings).order_by(OliveReadings.id.desc()).first().id

    def updateReading(self, reading_id, sample_time, nm_525_ON, nm_525_OFF, nm_680_ON, nm_680_OFF,
                       nm_740_ON, nm_740_OFF, nm_980_ON, nm_980_OFF, nm_1450_ON, nm_1450_OFF):
        reading = session.query(OliveReadings).filter_by(id=reading_id).first()
        if reading:
            reading.sampleTime = sample_time
            reading.nm_525_ON = nm_525_ON
            reading.nm_525_OFF = nm_525_OFF
            reading.nm_680_ON = nm_680_ON
            reading.nm_680_OFF = nm_680_OFF
            reading.nm_740_ON = nm_740_ON
            reading.nm_740_OFF = nm_740_OFF
            reading.nm_980_ON = nm_980_ON
            reading.nm_980_OFF = nm_980_OFF
            reading.nm_1450_ON = nm_1450_ON
            reading.nm_1450_OFF = nm_1450_OFF
            session.commit()

    def deleteReading(self, reading_id):
        reading = session.query(OliveReadings).filter_by(id=reading_id).first()
        if reading:
            session.delete(reading)
            session.commit()
    def truncate_table(self):
        session.query(OliveReadings).delete()
        session.commit()