from sqlalchemy.orm import Session
from models.affiliatedUniversityMasterModel import AffiliatedUniversityMaster
from sqlalchemy import select


class affiliatedUniversityMasterService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = (
            select(
                AffiliatedUniversityMaster.university_id_pk.label("id"),
                AffiliatedUniversityMaster.university_name.label("details"),
                AffiliatedUniversityMaster.dist_id_fk.label("districtId"),
            )
            .where(AffiliatedUniversityMaster.active_status == 1)
            .order_by(AffiliatedUniversityMaster.university_name.asc())
        )

        result = self.db.execute(stmt).mappings().all()
        return result
