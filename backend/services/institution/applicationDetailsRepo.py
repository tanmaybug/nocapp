from sqlalchemy.orm import Session
from sqlalchemy import select, join
from models.statusMasterModel import applicationStatusMaster
from models.applicationDetailsModel import NocApplicationDetails
from models.applictionTrackDetailsModel import applicationTrackDetails


class applicationDetailsService:
    def __init__(self, db: Session):
        self.db = db

    def get_application_data_by_id(self, regId: str):

        j = join(
            NocApplicationDetails,
            applicationStatusMaster,
            NocApplicationDetails.application_status
            == applicationStatusMaster.status_id_pk,
        )
        
        stmt = (
            select(NocApplicationDetails, applicationStatusMaster.status_description)
            .select_from(j)
            .where(NocApplicationDetails.noc_registration_id == regId)
            .where(NocApplicationDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result[0]
    
    def insert_data(
        self,
        application_data: NocApplicationDetails,
        track_data: applicationTrackDetails,
    ):
        try:
            self.db.add(application_data)
            self.db.add(track_data)
            self.db.commit()
            self.db.refresh(application_data)

            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False