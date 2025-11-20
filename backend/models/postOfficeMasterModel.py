from sqlalchemy import Column, Integer, String, SmallInteger, Sequence, ForeignKey
from config.DB.DBConfig import Base

class postOfficeMaster(Base):
    __tablename__ = "noc_post_office_master"
    __table_args__ = {"schema": "public"}

    po_id_pk = Column(
        Integer,
        Sequence('"Post_office_master_po_id_pk_seq"'),
        primary_key=True
    )
    po_name = Column(String(255), nullable=True)
    pin = Column(Integer, nullable=True)
    office_type = Column(String(255), nullable=True)
    dist_id_fk = Column(Integer, ForeignKey("public.noc_district_master.dist_id_pk"), nullable=True)
    state_id_fk = Column(Integer, nullable=True)  # Add ForeignKey if you have a state master table
    active_status = Column(SmallInteger, nullable=True)
