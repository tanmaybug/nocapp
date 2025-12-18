from models.applictionTrackDetailsModel import applicationTrackDetails
from helpers.dateHelper import date_time

def dtotodb(regId: str, client_ip:str) -> applicationTrackDetails:
    result = applicationTrackDetails(
        noc_registration_id=regId,
        status=1,
        remarks="Registration Done",
        insert_date=date_time(),
        insert_ip=client_ip,
        active_status=1,
    )
    return result
