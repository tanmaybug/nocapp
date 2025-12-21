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


def save_file_dtotodb(
    existing_data: uploadDocumentDetails, docTypeId: int
) -> uploadDocumentDetails:
    existing_data.document_id_fk = docTypeId

    return existing_data
