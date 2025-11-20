from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, SMALLINT


class Login(Base):
    __tablename__ = "noc_stake_user_login"

    login_id_pk = Column(Integer, primary_key=True, nullable=False)
    stake_level_id_fk = Column(Integer)
    login_token = Column(String, nullable=False)
    stake_user = Column(String, nullable=False)
    stake_password = Column(String, nullable=False)
    active_status = Column(SMALLINT, server_default="1")
    forgot_password_flag = Column(SMALLINT, server_default="1")
    forgot_password_token = Column(String, nullable=False)
