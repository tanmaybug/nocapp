from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class stakeLevel(Base):
    __tablename__ = "noc_stake_level"
    __table_args__ = {"schema": "public"}

    stake_level_id_pk = Column(
        Integer,
        Sequence("mis_stake_level_stake_level_id_pk_seq"),
        primary_key=True
    )
    stake_level_type_id_fk = Column(Integer, nullable=True)  # Can be ForeignKey later
    stake_level_abbreviation = Column(String(255), nullable=True)
    stake_level_description = Column(String(255), nullable=True)
    stake_level_master_pass = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
    priority = Column(SmallInteger, nullable=True)
