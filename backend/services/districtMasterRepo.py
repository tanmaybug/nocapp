from sqlalchemy.orm import Session
from models.districtMasterModel import districtMaster
from sqlalchemy import select

class districtMasterService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = (
            select(
                districtMaster.dist_id_pk.label("id"),
                districtMaster.dist_name.label("details"),
            )
            .where(districtMaster.active_status == 1)
            .order_by(districtMaster.dist_name.asc())
        )
        
        result = self.db.execute(stmt).mappings().all()
        return result
