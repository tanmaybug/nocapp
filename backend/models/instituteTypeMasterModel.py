from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class instituteTypeMaster(Base):
    __tablename__ = "noc_institute_type_master"
    __table_args__ = {"schema": "public"}

    institution_type_id_pk = Column(
        Integer,
        Sequence("institute_type_master_institution_type_id_pk_seq"),
        primary_key=True
    )
    institution_type_name = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)

    
