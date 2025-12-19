from sqlalchemy.orm import Session
from sqlalchemy import select
from models.applictionTrackDetailsModel import applicationTrackDetails

class applicationTrackService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self, regId: str):
        stmt = (
            select(applicationTrackDetails)
            .where(applicationTrackDetails.noc_registration_id == regId)
            .where(applicationTrackDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
