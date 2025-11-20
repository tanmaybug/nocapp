from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text,SMALLINT


class Post(Base):
    __tablename__ = "test_table"

    test_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    active_status = Column(SMALLINT, server_default="1")
    create_datetime = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    create_ip = Column(String,nullable=False)
