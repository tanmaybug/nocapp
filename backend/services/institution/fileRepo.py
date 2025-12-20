from sqlalchemy.orm import Session
from sqlalchemy import select
from models.uploadDocumentDetailsModel import uploadDocumentDetails


class FileService:
    def __init__(self, db: Session):
        self.db = db

    def get_unsaved_data(self,fileId:int, regId: str):
        stmt = (
            select(uploadDocumentDetails)
            .where(uploadDocumentDetails.upload_document_id_pk == fileId)
            .where(uploadDocumentDetails.noc_registration_id == regId)
            .where(uploadDocumentDetails.document_id_fk == 0)
            .where(uploadDocumentDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
    
    def update_doc_type(self, file_data: uploadDocumentDetails):
        try:
            self.db.add(file_data)
            self.db.commit()
            self.db.refresh(file_data)

            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False
