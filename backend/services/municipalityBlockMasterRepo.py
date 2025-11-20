from sqlalchemy.orm import Session
from models.municipalityBlockMasterModel import municipalityBlockMaster
from sqlalchemy import select

class municipalityService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = (
            select(
                municipalityBlockMaster.muni_block_id_pk.label("id"),
                municipalityBlockMaster.muni_block_name.label("details"),
                municipalityBlockMaster.sub_div_id_fk.label("subDivId"),
            )
            .where(municipalityBlockMaster.active_status == 1)
            .order_by(municipalityBlockMaster.muni_block_name.asc())
        )

        result = self.db.execute(stmt).mappings().all()
        return result
