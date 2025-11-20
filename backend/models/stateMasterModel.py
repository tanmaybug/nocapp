from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class stateMaster(Base):
    __tablename__ = "noc_state_master"
    __table_args__ = {"schema": "public"}

    state_id_pk = Column(
        Integer,
        Sequence("state_master_state_id_pk_seq"),
        primary_key=True
    )
    state_name = Column(String(255), nullable=True)
    state_lgd_code = Column(Integer, nullable=True)
    active_status = Column(SmallInteger, nullable=True)
