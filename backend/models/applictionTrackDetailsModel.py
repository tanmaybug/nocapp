from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, SMALLINT
from sqlalchemy.sql import func

class applicationTrackDetails(Base):
    __tablename__ = "noc_application_track_details"

    application_track_id_pk = Column(Integer, primary_key=True, nullable=False)
    noc_registration_id = Column(String, nullable=False)
    status = Column(SMALLINT, nullable=False)
    remarks = Column(String, nullable=False)
    insert_date = Column(TIMESTAMP, server_default=func.now())
    insert_ip = Column(String(15))
    active_status = Column(SMALLINT, default=1)
