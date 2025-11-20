from sqlalchemy.orm import Session
from models.minorityTypeMasterModel import minorityTypeMaster
from sqlalchemy import select


class minorityTypeService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = select(
            minorityTypeMaster.minority_type_id_pk.label("id"),
            minorityTypeMaster.minority_type.label("details"),
        ).where(minorityTypeMaster.active_status == 1)

        result = self.db.execute(stmt).mappings().all()
        return result
