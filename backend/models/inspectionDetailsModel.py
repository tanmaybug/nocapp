from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, SMALLINT, Text
from sqlalchemy.sql import func

class inspectionDetails(Base):
    __tablename__ = "noc_inspection_details"

    inspection_id_pk = Column(Integer, primary_key=True, nullable=False)
    noc_registration_id = Column(String, nullable=False)
    inspection_date = Column(String, nullable=False)
    inspection_feedback = Column(Text, nullable=False)
    inspection_document = Column(String, nullable=False)
    active_status = Column(SMALLINT, nullable=False)
    loi_or_noc = Column(SMALLINT, nullable=False)
    insert_time = Column(TIMESTAMP, server_default=func.now())
    insert_ip = Column(String(15))
    feedback_date = Column(String, nullable=False)
    inspection_set_by = Column(String, nullable=False)
    
