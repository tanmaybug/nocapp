from sqlalchemy.orm import Session
from sqlalchemy import select
from models.applictionTrackDetailsModel import applicationTrackDetails


class applicationTrackService:
    def __init__(self, db: Session):
        self.db = db

    def get_track_data_by_applicant_id(self, regId: str):
        stmt = (
            select(
                applicationTrackDetails.application_track_id_pk,
                applicationTrackDetails.status,
                applicationTrackDetails.remarks,
                applicationTrackDetails.insert_date,
            )
            .where(applicationTrackDetails.noc_registration_id == regId)
            .where(applicationTrackDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
