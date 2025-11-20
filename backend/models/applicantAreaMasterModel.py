from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, SMALLINT,float


class ApplicantAreaMaster(Base):
    __tablename__ = "noc_applicant_area_master"

    applicant_area_id_pk = Column(Integer, primary_key=True, nullable=False)
    area_name = Column(String, nullable=False)
    student_name = Column(String, nullable=False)
    amount = Column(float, nullable=False)
    geographic_area_id_fk = Column(Integer, nullable=False)
    active_status = Column(SMALLINT, nullable=False)
   