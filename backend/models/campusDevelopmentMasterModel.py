from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, SMALLINT,Text,float


class campusDevelopmentMaster(Base):
    __tablename__ = "noc_campus_development_master"

    campus_development_master_pk = Column(Integer, primary_key=True, nullable=False)
    campus_development_description = Column(String, nullable=False)
    active_status = Column(SMALLINT, nullable=False)
   

   