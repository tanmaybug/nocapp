from sqlalchemy import Column, Integer, String, SmallInteger, Sequence, TIMESTAMP
from config.DB.DBConfig import Base

class sessionMaster(Base):
    __tablename__ = "noc_session_master"
    __table_args__ = {"schema": "public"}

    session_id_pk = Column(
        Integer,
        Sequence("mis_session_master_session_id_pk_seq"),
        primary_key=True
    )
    session_description = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
    entry_time = Column(TIMESTAMP, nullable=True)
    stack_level_id_fk = Column(Integer, nullable=True)  # You can add ForeignKey if needed
    entry_ip = Column(String(15), nullable=True)
