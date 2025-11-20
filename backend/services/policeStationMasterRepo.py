from sqlalchemy.orm import Session
from models.policeStationMasterModel import policeStationMaster
from sqlalchemy import select


class policeStationMasterService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        stmt = (
            select(
                policeStationMaster.police_station_id_pk.label("id"),
                policeStationMaster.police_station_name.label("details"),
            )
            .where(policeStationMaster.active_status == 1)
            .order_by(policeStationMaster.police_station_name.asc())
        )

        result = self.db.execute(stmt).mappings().all()
        return result
