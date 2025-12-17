from sqlalchemy.orm import Session
from sqlalchemy import select
from models.inspectionDetailsModel import inspectionDetails


class applicationService:
    def __init__(self, db: Session):
        self.db = db

    def get_pending_application_data(self):
        stmt = (
            select(inspectionDetails)
            .where(inspectionDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
    
    def get_inprocess_application_data(self):
        stmt = (
            select(inspectionDetails)
            .where(inspectionDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
    
    def get_complete_application_data(self):
        stmt = (
            select(inspectionDetails)
            .where(inspectionDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
