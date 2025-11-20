from sqlalchemy.orm import Session
from models.uploadDocumentDetailsModel import uploadDocumentDetails

class form3Service:
    def __init__(self, db: Session):
        self.db = db

    def insert_data(
        self,
        form_data: uploadDocumentDetails,
    ):
        try:
            self.db.add(form_data)
            self.db.commit()
            self.db.refresh(form_data)
            return form_data
        except Exception as e:
            print(e)
            self.db.rollback()
            return False