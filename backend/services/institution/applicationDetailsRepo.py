from sqlalchemy.orm import Session
from sqlalchemy import select
from models.applicationDetailsModel import NocApplicationDetails
from models.applictionTrackDetailsModel import applicationTrackDetails

class applicationDetailsService:
    def __init__(self, db: Session):
        self.db = db

    def get_application_data_by_id(self, regId: str):
        stmt = (
            select(NocApplicationDetails)
            .where(NocApplicationDetails.noc_registration_id == regId)
            .where(NocApplicationDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
    
    def insert_data(
        self,
        application_data: NocApplicationDetails,
        track_data: applicationTrackDetails,
    ):
        try:
            self.db.add(application_data)
            self.db.add(track_data)
            self.db.commit()
            self.db.refresh(application_data)

            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False