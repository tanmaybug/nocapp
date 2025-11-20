from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class subjectMaster(Base):
    __tablename__ = "noc_subject_master"
    __table_args__ = {"schema": "public"}

    subject_id_pk = Column(
        Integer,
        Sequence("mis_subject_master_subject_id_pk_seq"),
        primary_key=True
    )
    subject_name = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
