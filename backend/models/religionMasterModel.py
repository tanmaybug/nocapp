from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base


class religionMaster(Base):
    __tablename__ = "noc_religion_master"
    __table_args__ = {"schema": "public"}

    religion_id_pk = Column(
        Integer,
        Sequence("noc_religion_master_religion_id_pk_seq"),
        primary_key=True,
    )
    religion_name = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
