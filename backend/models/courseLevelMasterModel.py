from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, SMALLINT,Text,float


class courseLevelMaster(Base):
    __tablename__ = "noc_course_level_master"

    course_level_id_pk = Column(Integer, primary_key=True, nullable=False)
    course_level_name = Column(String, nullable=False)
    active_status = Column(SMALLINT, nullable=False)
   