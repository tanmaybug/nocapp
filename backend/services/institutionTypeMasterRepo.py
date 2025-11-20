from sqlalchemy.orm import Session
from models.instituteTypeMasterModel import instituteTypeMaster
from sqlalchemy import select


class institutionTypeMasterService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = (
            select(
                instituteTypeMaster.institution_type_id_pk.label("id"),
                instituteTypeMaster.institution_type_name.label("details"),
            )
            .where(instituteTypeMaster.active_status == 1)
            .order_by(instituteTypeMaster.institution_type_name.asc())
        )

        result = self.db.execute(stmt).mappings().all()
        return result
