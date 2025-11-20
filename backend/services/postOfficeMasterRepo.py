from sqlalchemy.orm import Session
from models.postOfficeMasterModel import postOfficeMaster
from sqlalchemy import select

class postOfficeMasterService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        return (
            self.db.query(postOfficeMaster)
            .filter(postOfficeMaster.active_status == 1)
            .all()
        )
    
    def get_data_by_pin_code(self, pin):
        stmt = (
            select(
                postOfficeMaster.po_id_pk.label("id"),
                postOfficeMaster.po_name.label("details"),
            )
            .where(postOfficeMaster.active_status == 1)
            .where(postOfficeMaster.pin == pin)
            .order_by(postOfficeMaster.po_name.asc())
        )

        result = self.db.execute(stmt).mappings().all()
        return result
