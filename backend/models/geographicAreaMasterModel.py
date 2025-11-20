from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class geographicAreaMaster(Base):
    __tablename__ = "noc_geographic_area_master"
    __table_args__ = {"schema": "public"}

    geographic_area_id_pk = Column(
        Integer,
        Sequence("mis_geographic_area_master_geographic_area_id_pk_seq"),
        primary_key=True
    )
    geographic_area_type_name = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
