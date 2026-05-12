from sqlalchemy.orm import Session
from models.applicantDesignationMasterModel import applicantDesignationMaster
from sqlalchemy import select


class designationMasterService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = (
            select(
                applicantDesignationMaster.applicant_designation_id_pk.label("id"),
                applicantDesignationMaster.applicant_designation_name.label("details"),
            )
            .where(applicantDesignationMaster.active_status == 1)
            .order_by(applicantDesignationMaster.applicant_designation_name.asc())
        )

        result = self.db.execute(stmt).mappings().all()
        return result
