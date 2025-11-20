from sqlalchemy.orm import Session
from models.applicationDetailsModel import NocApplicationDetails
from fastapi.encoders import jsonable_encoder

class form1Service:
    def __init__(self, db: Session):
        self.db = db

    def insert_data(
        self,
        #noc_registration_id: 1234,
        form_data: NocApplicationDetails,
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

