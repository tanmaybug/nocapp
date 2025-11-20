from sqlalchemy.orm import Session
from dtos.form2DTO import Form2
from models.applicationDetailsModel import NocApplicationDetails

class form2Service:
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

    def update_data(self, form_data: Form2):
        """
        Updates an existing NOC Application record (Form2 data) using regId.
        """

        # Step 3: Commit & refresh
        try:
            self.db.add(form_data)
            self.db.commit()
            self.db.refresh(form_data)
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False

