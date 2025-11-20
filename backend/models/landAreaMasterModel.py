from sqlalchemy import Column, Integer, String, SmallInteger, Sequence, ForeignKey
from config.DB.DBConfig import Base

class landAreaMaster(Base):
    __tablename__ = "noc_land_area_master"
    __table_args__ = {"schema": "public"}

    land_area_id_pk = Column(
        Integer,
        Sequence("land_area_master_land_area_id_pk_seq"),
        primary_key=True
    )
    geographic_area_id_fk = Column(Integer, ForeignKey("public.noc_geographic_area_master.geographic_area_id_pk"), nullable=True)
    land_area = Column(String, nullable=True)
    active_status = Column(SmallInteger, nullable=True)