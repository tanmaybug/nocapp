from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class municipalityBlockMaster(Base):
    __tablename__ = "noc_municipality_block_master"

    muni_block_id_pk = Column(
        Integer,
        Sequence("block_master_block_id_pk_seq"),
        primary_key=True
    )
    muni_block_name = Column(String(255), nullable=True)
    muni_block_lgd_code = Column(Integer, nullable=True)
    sub_div_id_fk = Column(Integer, nullable=True)         # Add ForeignKey if block table exists
    active_status = Column(SmallInteger, nullable=True)