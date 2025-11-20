from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class qualifyingMaster(Base):
    __tablename__ = "noc_qualifying_master"
    __table_args__ = {"schema": "public"}

    qualifying_id_pk = Column(
        Integer,
        Sequence("qualifying_master_qualifying_id_pk_seq"),
        primary_key=True
    )
    qualifying_name = Column(String(255), nullable=True)
    dpi_applicable_status = Column(Integer, nullable=True)
    dme_applicable_status = Column(Integer, nullable=True)
    dte_applicable_status = Column(Integer, nullable=True)
    dtet_applicable_status = Column(Integer, nullable=True)
    active_status = Column(SmallInteger, nullable=True)
    qualifying_percentage = Column(Integer, nullable=True)
