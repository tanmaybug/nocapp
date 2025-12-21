from sqlalchemy.orm import Session
from sqlalchemy import select, join
from models.applicationDetailsModel import NocApplicationDetails
from models.NOCRegistrationTableModel import NOCRegistration


class applicationService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_application_data_by_id(self, regId: str):
        stmt = (
            select(NocApplicationDetails)
            .where(NocApplicationDetails.noc_registration_id == regId)
            .where(NocApplicationDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
    
    def get_pending_application_data(self):
        j = join(
            NocApplicationDetails,
            NOCRegistration,
            NocApplicationDetails.noc_registration_id == NOCRegistration.noc_registration_id,
        )

        stmt = (
            select(
                NocApplicationDetails.noc_registration_id,
                NOCRegistration.institute_name,
                NOCRegistration.applicant_name,
                NOCRegistration.applicant_mobile,
                NOCRegistration.applicant_email_id,
            )
            .select_from(j)
            .where(NocApplicationDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
    
    def get_pending_application_data_old(self):
        stmt = (
            select(NocApplicationDetails)
            .where(NocApplicationDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
    
    def get_inprocess_application_data(self):
        j = join(
            NocApplicationDetails,
            NOCRegistration,
            NocApplicationDetails.noc_registration_id
            == NOCRegistration.noc_registration_id,
        )

        stmt = (
            select(
                NocApplicationDetails.noc_registration_id,
                NOCRegistration.institute_name,
                NOCRegistration.applicant_name,
                NOCRegistration.applicant_mobile,
                NOCRegistration.applicant_email_id,
            )
            .select_from(j)
            .where(NocApplicationDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
    
    def get_complete_application_data(self):
        j = join(
            NocApplicationDetails,
            NOCRegistration,
            NocApplicationDetails.noc_registration_id
            == NOCRegistration.noc_registration_id,
        )

        stmt = (
            select(
                NocApplicationDetails.noc_registration_id,
                NOCRegistration.institute_name,
                NOCRegistration.applicant_name,
                NOCRegistration.applicant_mobile,
                NOCRegistration.applicant_email_id,
            )
            .select_from(j)
            .where(NocApplicationDetails.active_status == 1)
        )

        result = self.db.execute(stmt).mappings().all()
        return result
