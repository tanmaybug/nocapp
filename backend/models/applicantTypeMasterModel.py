from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, SMALLINT,Text,float


class applicantTypeMaster(Base):
    __tablename__ = "noc_applicant_type_master"

    applicant_type_id_pk = Column(Integer, primary_key=True, nullable=False)
    applicant_type = Column(String, nullable=False)
    applicant_description = Column(String, nullable=False)
    active_status = Column(SMALLINT, nullable=False)
   