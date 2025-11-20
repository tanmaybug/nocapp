from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class institutionEstablishmentTypeMaster(Base):
    __tablename__ = "noc_institution_establishment_type_master"
    __table_args__ = {"schema": "public"}

    establishment_type_id_pk = Column(
        Integer,
        Sequence("mis_institution_establishment_type_establishment_type_id_pk_seq"),
        primary_key=True
    )
    establishment_type_name = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
