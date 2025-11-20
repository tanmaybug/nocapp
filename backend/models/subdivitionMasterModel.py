from sqlalchemy import Column, Integer, String, Sequence,SMALLINT
from config.DB.DBConfig import Base

class subdivisionMaster(Base):
    __tablename__ = "noc_subdivision_master"

    sub_div_id_pk = Column(
        Integer,
        Sequence("subdivition_master_sub_div_id_pk_seq"),
        primary_key=True
    )
    sub_div_name = Column(String(255), nullable=True)
    sub_div_lgd_code = Column(Integer, nullable=True)
    dist_id_fk = Column(Integer, nullable=True)  # Add ForeignKey if linked to noc_district_master
    active_status = Column(SMALLINT, nullable=True)