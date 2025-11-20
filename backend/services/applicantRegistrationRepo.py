from sqlalchemy.orm import Session
from models.NOCRegistrationTableModel import NOCRegistration
from models.loginTableModel import Login


class applicantRegistrationService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        return (
            self.db.query(NOCRegistration)
            .filter(NOCRegistration.active_status == 1)
            .all()
        )

    def insert_data(
        self,
        registration_data: NOCRegistration,
        login_data: Login,
    ):
        try:
            self.db.add(registration_data)
            self.db.add(login_data)
            self.db.commit()
            self.db.refresh(registration_data)
            # return registration_data.applicant_record_id_pk # Last Insert Id
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False
