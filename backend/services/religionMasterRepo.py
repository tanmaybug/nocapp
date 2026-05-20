from sqlalchemy.orm import Session
from models.religionMasterModel import religionMaster
from sqlalchemy import select


class religionMasterService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = (
            select(
                religionMaster.religion_id_pk.label("id"),
                religionMaster.religion_name.label("details"),
            )
            .where(religionMaster.active_status == 1)
            .order_by(religionMaster.religion_name.asc())
        )

        result = self.db.execute(stmt).mappings().all()
        if result:
            return result
        else:
            return None
