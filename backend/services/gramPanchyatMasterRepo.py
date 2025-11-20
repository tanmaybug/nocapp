from sqlalchemy.orm import Session
from models.gramPanchyatMasterModel import gramPanchyatMaster
from sqlalchemy import select

class gramPanchyatService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = (
            select(
                gramPanchyatMaster.gp_id_pk.label("id"),
                gramPanchyatMaster.gp_name.label("details"),
                gramPanchyatMaster.block_id_fk.label("blockId"),
            )
            .where(gramPanchyatMaster.active_status == 1)
            .order_by(gramPanchyatMaster.gp_name.asc())
        )

        result = self.db.execute(stmt).mappings().all()
        return result
    
    def get_data_by_blockid(self,blockId):
        stmt = (
            select(
                gramPanchyatMaster.gp_id_pk.label("id"),
                gramPanchyatMaster.gp_name.label("details"),
            )
            .where(gramPanchyatMaster.active_status == 1)
            .where(gramPanchyatMaster.block_id_fk == blockId)
            .order_by(gramPanchyatMaster.gp_name.asc())
        )

        result = self.db.execute(stmt).mappings().all()
        return result
