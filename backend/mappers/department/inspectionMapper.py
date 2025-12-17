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
    data: InspectionFeedbackRequest, client_ip: str
) -> inspectionDetails:
    result = inspectionDetails(
        noc_registration_id=data.nocRegId,
        inspection_feedback = data.remarks,
        insert_ip=client_ip,
        insert_time=date_time(),
    )

    return result