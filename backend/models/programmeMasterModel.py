from sqlalchemy import Column, Integer, String, SmallInteger, Sequence, ForeignKey
from config.DB.DBConfig import Base

class programmeMaster(Base):
    __tablename__ = "noc_programme_master"
    __table_args__ = {"schema": "public"}

    programme_id_pk = Column(
        Integer,
        Sequence("mis_programme_master_programme_id_pk_seq"),
        primary_key=True
    )
    programme_name = Column(String(255), nullable=True)
    programme_description = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
    course_level_id_fk = Column(Integer, ForeignKey("public.noc_course_level_master.course_level_id_pk"), nullable=True)
    integrated_general_status = Column(Integer, nullable=True)
