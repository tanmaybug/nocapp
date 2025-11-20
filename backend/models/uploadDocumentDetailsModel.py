from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, SMALLINT


class uploadDocumentDetails(Base):
    __tablename__ = "noc_upload_document_details"

    upload_document_id_pk = Column(Integer, primary_key=True, nullable=False)
    noc_registration_id = Column(String, nullable=False)
    document_id_fk = Column(Integer, nullable=False)
    uploaded_document_name = Column(String, nullable=False)
    active_status = Column(SMALLINT, nullable=False)
    upload_time = Column(TIMESTAMP, nullable=True)
    upload_ip = Column(String(15), nullable=True)
