from sqlalchemy.orm import Session
from sqlalchemy import select
from models.inspectionDetailsModel import inspectionDetails

class inspectionService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self, nocRegId):
        stmt = (
            select(
                inspectionDetails.noc_registration_id.label("nocRegId"),
                inspectionDetails.inspection_date.label("date"),
                inspectionDetails.inspection_feedback.label("feedback"),
                inspectionDetails.loi_or_noc.label("loiOrNoc"),
                inspectionDetails.inspection_document.label("document"),
                inspectionDetails.feedback_date.label("feedbackDate"),
            )
            .where(inspectionDetails.noc_registration_id == nocRegId)
            .where(inspectionDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result

    def insert_data(self, inspection_data: inspectionDetails):
        try:
            self.db.add(inspection_data)
            self.db.commit()
            self.db.refresh(inspection_data)
            
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False
