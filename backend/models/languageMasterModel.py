from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base


class languageMaster(Base):
    __tablename__ = "noc_language_master"
    __table_args__ = {"schema": "public"}

    language_id_pk = Column(
        Integer,
        Sequence("noc_language_master_language_id_pk_seq"),
        primary_key=True,
    )
    language_name = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
