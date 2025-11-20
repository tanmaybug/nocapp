from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, SMALLINT,Text


class StudentDetails(Base):
    __tablename__ = "student_details"

    student_id_pk = Column(Integer, primary_key=True, nullable=False)
    student_registration_no = Column(String, nullable=False)
    student_name = Column(String, nullable=False)
    student_phone_number = Column(String, nullable=False)
    student_email_id = Column(String, nullable=False)
    student_address = Column(Text, nullable=False)
    student_gender = Column(SMALLINT, nullable=False)
    student_hobby = Column(Text, nullable=False)
    student_photo = Column(String, nullable=False)
    student_sign = Column(String, nullable=False)
    active_status = Column(SMALLINT, server_default="1")
    create_datetime = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    create_ip = Column(String, nullable=False)
