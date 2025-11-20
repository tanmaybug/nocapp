from sqlalchemy import Column, Integer, SmallInteger, Sequence
from config.DB.DBConfig import Base

class feeMaster(Base):
    __tablename__ = "noc_fee_master"
    __table_args__ = {"schema": "public"}

    fee_id_pk = Column(
        Integer,
        Sequence("fee_master_fee_id_pk_seq"),
        primary_key=True
    )
    course_id_fk = Column(Integer, nullable=True)       # Optional: Add ForeignKey
    fee_type_id_fk = Column(Integer, nullable=True)     # Optional: Add ForeignKey
    fee = Column(Integer, nullable=True)
    session_id_fk = Column(Integer, nullable=True)      # Optional: Add ForeignKey
    active_status = Column(SmallInteger, nullable=True)