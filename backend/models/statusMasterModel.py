from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String,SMALLINT


class applicationStatusMaster(Base):
    __tablename__ = "noc_status_master"

    status_id_pk = Column(Integer, primary_key=True, nullable=False)
    status_description = Column(String, nullable=False)
    active_status = Column(SMALLINT, nullable=False)
