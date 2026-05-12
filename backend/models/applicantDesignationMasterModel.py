from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base


class applicantDesignationMaster(Base):
    __tablename__ = "noc_applicant_designation_master"
    __table_args__ = {"schema": "public"}

    applicant_designation_id_pk = Column(
        Integer,
        Sequence("noc_applicant_designation_maste_applicant_designation_id_pk_seq"),
        primary_key=True,
    )
    applicant_designation_name = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
