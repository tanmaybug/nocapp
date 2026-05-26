from sqlalchemy.orm import Session
from models.languageMasterModel import languageMaster
from sqlalchemy import select


class languageMasterService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = (
            select(
                languageMaster.language_id_pk.label("id"),
                languageMaster.language_name.label("details"),
            )
            .where(languageMaster.active_status == 1)
            .order_by(languageMaster.language_name.asc())
        )

        result = self.db.execute(stmt).mappings().all()
        if result:
            return result
        else:
            return None
