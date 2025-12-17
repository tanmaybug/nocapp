from dtos.department.inspectionRequestDTO import (
    SetInspectionRequest,
    InspectionFeedbackRequest,
)
from models.inspectionDetailsModel import inspectionDetails
from helpers.dateHelper import date_time

def dtotodb_insert(
    data: SetInspectionRequest, userId: str, client_ip: str
) -> inspectionDetails:
    result = inspectionDetails(
        noc_registration_id=data.nocRegId,
        inspection_date=data.date,
        insert_ip=client_ip,
        insert_time=date_time(),
        inspection_set_by=userId,
    )

    return result

def dtotodb_update(
    data: InspectionFeedbackRequest, existing_data: inspectionDetails
) -> inspectionDetails:
    if data.remarks is not None:
        existing_data.inspection_feedback = data.remarks
    if data.status is not None:
        existing_data.loi_or_noc = data.status
    
    existing_data.feedback_date = date_time()

    return existing_data

def dtotodb_document_update(
    existing_data: inspectionDetails, file_path:str
) -> inspectionDetails:
    
    existing_data.inspection_document = file_path
    existing_data.feedback_date = date_time()

    return existing_data