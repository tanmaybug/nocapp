from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class stakeLevelType(Base):
    __tablename__ = "noc_stake_level_type"
    __table_args__ = {"schema": "public"}

    stake_level_type_id_pk = Column(
        Integer,
        Sequence("mis_stake_level_type_stake_level_type_id_pk_seq"),
        primary_key=True
    )
    stake_level_type_name = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
    priority = Column(SmallInteger, nullable=True)
