from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class sourseFundMaster(Base):
    __tablename__ = "noc_sourse_fund_master"
    __table_args__ = {"schema": "public"}

    sourse_fund_id_pk = Column(
        Integer,
        Sequence("sourse_fund_master_sourse_fund_id_pk_seq"),
        primary_key=True
    )
    sourse_fund_description = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
