from models.applictionTrackDetailsModel import applicationTrackDetails
from helpers.dateHelper import date_time

def dtotodb(data) -> applicationTrackDetails:
    result = applicationTrackDetails(
        noc_registration_id=data["nocRegId"],
        status=data["status"],
        remarks=data["remarks"],
        insert_date=date_time(),
        insert_ip=data['ip'],
        active_status=1,
    )
    return result
