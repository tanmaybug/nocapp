from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, SMALLINT, TIMESTAMP


class FundUtilization(Base):
    __tablename__ = "noc_fund_utilisation_details"

    fund_resources_id_pk = Column(Integer, primary_key=True, nullable=False)
    noc_registration_id = Column(String)
    financial_resources_year = Column(String)
    financial_resources_fund = Column(String)
    financial_resources_utilisation = Column(String)
    active_status = Column(SMALLINT, server_default="1")
    fund_resources_entry_time =Column(TIMESTAMP, nullable=True)
    fund_resources_entry_ip = Column(String, nullable=False)
