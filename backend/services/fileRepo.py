from sqlalchemy.orm import Session
from models.uploadDocumentDetailsModel import uploadDocumentDetails
from sqlalchemy import select


class fileService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self, fileId):
        stmt = (
            select(uploadDocumentDetails.uploaded_document_name)
            .where(uploadDocumentDetails.active_status == 1)
            .where(uploadDocumentDetails.upload_document_id_pk == fileId)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
