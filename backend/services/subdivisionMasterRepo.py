from sqlalchemy.orm import Session
from models.subdivitionMasterModel import subdivisionMaster
from sqlalchemy import select

class subDevisionMasterService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = (
            select(
                subdivisionMaster.sub_div_id_pk.label("id"),
                subdivisionMaster.sub_div_name.label("details"),
                subdivisionMaster.dist_id_fk.label("districtId"),
            )
            .where(subdivisionMaster.active_status == 1)
            .order_by(subdivisionMaster.sub_div_name.asc())
        )

        result = self.db.execute(stmt).mappings().all()
        return result
