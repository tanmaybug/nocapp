from sqlalchemy.orm import Session
from models.assemblyConstitutionMasterModel import assemblyConstitutionMaster
from sqlalchemy import select

class assemblyConstituencyService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = (
            select(
                assemblyConstitutionMaster.assembly_constituency_id_pk.label("id"),
                assemblyConstitutionMaster.assembly_constituency_name.label("details"),
                assemblyConstitutionMaster.dist_id_fk.label("districtId"),
            )
            .where(assemblyConstitutionMaster.active_status == 1)
            .order_by(assemblyConstitutionMaster.assembly_constituency_name.asc())
        )

        result = self.db.execute(stmt).mappings().all()
        return result
