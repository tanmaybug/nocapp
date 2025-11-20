from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, SMALLINT,Text,float


class blockMaster(Base):
    __tablename__ = "noc_block_master"

    block_id_pk = Column(Integer, primary_key=True, nullable=False)
    block_name = Column(String, nullable=False)
    block_lgd_code = Column(Integer, nullable=False)
    sub_div_id_fk = Column(Integer, nullable=False)
    active_status = Column(SMALLINT, nullable=False)
   