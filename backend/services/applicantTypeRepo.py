from sqlalchemy.orm import Session
from models.applicantTypeMasterTableModel import applicantTypeMaster
from sqlalchemy import select

class applicantTypeService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = select(
            applicantTypeMaster.applicant_type_id_pk.label("id"),
            applicantTypeMaster.applicant_type.label("details"),
        ).where(applicantTypeMaster.active_status == 1)

        result = self.db.execute(stmt).mappings().all()
        return result
