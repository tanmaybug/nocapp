from sqlalchemy.orm import Session
from models.applictionTrackDetailsModel import applicationTrackDetails
from models.NOCRegistrationTableModel import NOCRegistration
from models.loginTableModel import Login
from models.applicationDetailsModel import NocApplicationDetails
from sqlalchemy import select


class applicantRegistrationService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        return (
            self.db.query(NOCRegistration)
            .filter(NOCRegistration.active_status == 1)
            .all()
        )
    
    def check_reg_id(self,regId:str)->bool:
        stmt = (
            select(NocApplicationDetails)
            .where(NocApplicationDetails.noc_registration_id == regId)
        )

        result = self.db.execute(stmt).mappings().all()
        if result:
            return True
        else:
            return False

    def insert_data(
        self,
        registration_data: NOCRegistration,
        login_data: Login,
        from1_data: NocApplicationDetails,
        track_data: applicationTrackDetails,
    ):
        try:
            self.db.add(registration_data)
            self.db.add(login_data)
            self.db.add(from1_data)
            self.db.add(track_data)
            self.db.commit()
            self.db.refresh(registration_data)
            # return registration_data.applicant_record_id_pk # Last Insert Id
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False
