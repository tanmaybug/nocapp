from models.uploadDocumentDetailsModel import uploadDocumentDetails
from helpers.dateHelper import date_time

def dtotodb(data) -> uploadDocumentDetails:
    result = uploadDocumentDetails(
        noc_registration_id=data["regId"],
        document_id_fk=data["documentId"],
        uploaded_document_name=data["documentName"],
        active_status=1,
        upload_time=date_time(),
        upload_ip=data["ip"],
    )

    return result
