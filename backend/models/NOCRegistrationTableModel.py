from sqlalchemy import (
    Column,
    Integer,
    String,
    SmallInteger,
    Text,
    TIMESTAMP,
)
from config.DB.DBConfig import Base


class NOCRegistration(Base):
    __tablename__ = "noc_registration"

    applicant_record_id_pk = Column(Integer, primary_key=True, nullable=False)
    applicant_type_id_fk = Column(Integer, nullable=True)
    applicant_name = Column(String(255), nullable=True)
    applicant_mobile = Column(Integer, nullable=True)
    applicant_dst_id_fk = Column(Integer, nullable=True)
    applicant_subdiv_id_fk = Column(Integer, nullable=True)
    applicant_police_station_id_fk = Column(Integer, nullable=True)
    applicant_post_office_id_fk = Column(Integer, nullable=True)
    applicant_assembly_constitution_id_fk = Column(Integer, nullable=True)
    applicant_pin = Column(Integer, nullable=True)
    applicant_block_mun_id_fk = Column(Integer, nullable=True)
    applicant_city = Column(String(255), nullable=True)
    socities_rigistration_act_flag = Column(SmallInteger, nullable=True)
    minority_flag = Column(SmallInteger, nullable=True)
    minority_type_id_fk = Column(Integer, nullable=True)
    registration_no = Column(Text, nullable=True)
    registration_date = Column(Text, nullable=True)
    registration_place = Column(Text, nullable=True)
    details_minority_status = Column(Text, nullable=True)
    entry_time = Column(TIMESTAMP, nullable=True)
    entry_ip = Column(String(255), nullable=True)
    registration_acceptance_flag = Column(SmallInteger, nullable=True)
    institute_name = Column(String(255), nullable=True)
    aff_unv_id_fk = Column(Integer, nullable=True)
    inst_type_id_fk = Column(Integer, nullable=True)
    institution_dst_id_fk = Column(Integer, nullable=True)
    institution_subdi_id_fk = Column(Integer, nullable=True)
    institution_police_station_id_fk = Column(Integer, nullable=True)
    institution_block_id_fk = Column(Integer, nullable=True)
    institution_post_office_id_fk = Column(Integer, nullable=True)
    institution_pin = Column(Integer, nullable=True)
    institution_panchayat_id_fk = Column(Integer, nullable=True)
    institution_assembly_constitution_id_fk = Column(Integer, nullable=True)
    noc_registration_id = Column(String, nullable=True)
    applicant_address = Column(String, nullable=True)
    institution_address = Column(String, nullable=True)
    active_status = Column(SmallInteger, nullable=True)
