from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class NOCSpecialActivitiesMaster(Base):
    __tablename__ = "noc_special_activities_master"
    __table_args__ = {"schema": "public"}

    special_activities_id_pk = Column(
        Integer,
        Sequence("special_activities_master_special_activities_id_pk_seq"),
        primary_key=True
    )
    special_activities = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
