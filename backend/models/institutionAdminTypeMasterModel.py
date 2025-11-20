from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class institutionAdminTypeMaster(Base):
    __tablename__ = "noc_institution_admin_type_master"
    __table_args__ = {"schema": "public"}

    inst_admin_type_id_pk = Column(
        Integer,
        Sequence("institution_admin_type_master_inst_admin_type_id_pk_seq"),
        primary_key=True
    )
    inst_admin_type_id_name = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
