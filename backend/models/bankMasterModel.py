from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, SMALLINT,Text,float


class bankeMaster(Base):
    __tablename__ = "noc_bank_master"

    bank_id_pk = Column(Integer, primary_key=True, nullable=False)
    bank_name = Column(String, nullable=False)
    bank_code = Column(Integer, nullable=False)
    bank_ifsc = Column(String, nullable=False)
    digit_in_account_no = Column(Integer, nullable=False)
    active_status = Column(SMALLINT, nullable=False)

