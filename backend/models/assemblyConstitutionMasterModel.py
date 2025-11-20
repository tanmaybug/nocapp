from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, SMALLINT


class assemblyConstitutionMaster(Base):
    __tablename__ = "noc_assembly_constituency_master"

    assembly_constituency_id_pk = Column(Integer, primary_key=True, nullable=False)
    assembly_constituency_name = Column(String, nullable=False)
    assembly_constituency_lgd_code = Column(Integer, nullable=False)
    dist_id_fk = Column(Integer, nullable=False)
    active_status = Column(SMALLINT, nullable=False)