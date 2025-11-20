from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from config.DB.DBConfig import Base

class instituteMaster(Base):
    __tablename__ = "noc_institute_master"
    __table_args__ = {"schema": "public"}

    institution_id_pk = Column(
        Integer,
        Sequence("institute_master_institution_id_pk_seq"),
        primary_key=True
    )
    institution_name = Column(String(255), nullable=True)
    institution_code = Column(Integer, nullable=True)
    university_id_fk = Column(Integer, nullable=True)            # ForeignKey (optional)
    dist_id_fk = Column(Integer, nullable=True)                  # ForeignKey (optional)
    institution_latitute = Column(String(255), nullable=True)
    institution_longitute = Column(String(255), nullable=True)
    inst_admin_type_id_fk = Column(Integer, nullable=True)       # ForeignKey (optional)
    establishment_type_id_fk = Column(Integer, nullable=True)    # ForeignKey (optional)
    jdpi_id_fk = Column(Integer, nullable=True)                  # ForeignKey (optional)
    dte_applicable_status = Column(Integer, nullable=True)
    dpi_applicable_status = Column(Integer, nullable=True)
    active_status = Column(SmallInteger, nullable=True)

    