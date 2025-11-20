from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class districtMaster(Base):
    __tablename__ = "noc_district_master"
    __table_args__ = {"schema": "public"}

    dist_id_pk = Column(
        Integer,
        Sequence("district_master_dist_id_pk_seq"),
        primary_key=True
    )
    dist_name = Column(String(255), nullable=True)
    dist_lgd_code = Column(Integer, nullable=True)
    state_id_fk = Column(Integer, nullable=True)  # Add ForeignKey if needed
    active_status = Column(SmallInteger, nullable=True)