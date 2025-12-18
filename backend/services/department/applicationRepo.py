from sqlalchemy.orm import Session
from sqlalchemy import select
from models.applicationDetailsModel import NocApplicationDetails


class applicationService:
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

    def get_pending_application_data(self):
        stmt = (
            select(NocApplicationDetails)
            .where(NocApplicationDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
    
    def get_inprocess_application_data(self):
        stmt = (
            select(NocApplicationDetails)
            .where(NocApplicationDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
    
    def get_complete_application_data(self):
        stmt = (
            select(NocApplicationDetails)
            .where(NocApplicationDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
