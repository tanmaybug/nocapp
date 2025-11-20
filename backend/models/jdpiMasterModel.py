from sqlalchemy import Column, Integer, String, SmallInteger, Sequence, TIMESTAMP
from config.DB.DBConfig import Base

class JDpiMaster(Base):
    __tablename__ = "noc_jdpi_master"
    __table_args__ = {"schema": "public"}

    jdpi_id_pk = Column(
        Integer,
        Sequence("mis_jdpi_master_jdpi_id_pk_seq"),
        primary_key=True
    )
    stake_level_id_fk = Column(Integer, nullable=True)
    jdpi_code = Column(Integer, nullable=True)
    jdpi_type = Column(String(255), nullable=True)
    jdpi_mobile_no = Column(Integer, nullable=True)
    active_status = Column(SmallInteger, nullable=True)
    entry_ip = Column(String(15), nullable=True)
    entry_time = Column(TIMESTAMP, nullable=True)
    password_activation_token = Column(String(255), nullable=True)
    jdpi_first_name = Column(String(255), nullable=True)
    jdpi_middle_name = Column(String(255), nullable=True)
    jdpi_last_name = Column(String(255), nullable=True)
    jdpi_email_id = Column(String(255), nullable=True)
