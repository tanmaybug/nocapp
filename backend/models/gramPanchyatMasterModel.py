from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, SMALLINT


class gramPanchyatMaster(Base):
    __tablename__ = "noc_gram_panchyat_master"

    gp_id_pk = Column(Integer, primary_key=True, nullable=False)
    block_id_fk = Column(Integer, nullable=False)
    gp_code = Column(String, nullable=False)
    gp_name = Column(String, nullable=False)
    block_name = Column(String, nullable=False)
    district_name = Column(String, nullable=False)
    gp_lgd_code = Column(Integer, nullable=False)
    active_status = Column(SMALLINT, nullable=False)
