from typing import Optional
from sqlalchemy.orm import Session
from dtos.form1DTOcg import Form1
from mappers.form1Mapper import dbtodto
from models.applicationDetailsModel import NocApplicationDetails
#from fastapi.encoders import jsonable_encoder

class form1Service:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self, regId: str):
        # Fetch record
        record = (
            self.db.query(NocApplicationDetails)
            .filter_by(noc_registration_id=regId)
            .first()
        ) 

        if record:
            return record 
        else:
            return False

    def update_data(
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
        
    def get_application_by_reg_id(self, reg_id: str) -> Optional[Form1]:
            """
        Fetch application from DB and convert to DTO
        """
        # 1️⃣ Fetch from DB
            db_obj = (
                self.db
                .query(NocApplicationDetails)
                .filter(NocApplicationDetails.noc_registration_id == reg_id)
                .first()
            )

            if not db_obj:
                return None

            # 2️⃣ Convert DB model → DTO
            return dbtodto(db_obj)

