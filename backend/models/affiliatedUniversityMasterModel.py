from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, SMALLINT


class AffiliatedUniversityMaster(Base):
    __tablename__ = "noc_aff_university_master"

    university_id_pk = Column(Integer, primary_key=True, nullable=False)
    university_name = Column(String, nullable=False)
    dist_id_fk = Column(Integer, nullable=False)
    university_latitute = Column(String, nullable=False)
    university_longitute = Column(String, nullable=False)
    admin_type_id_fk = Column(Integer, nullable=False)
    active_status = Column(SMALLINT, nullable=False)
    university_code = Column(String, nullable=False)
