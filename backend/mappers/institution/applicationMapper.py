from models.applicationDetailsModel import NocApplicationDetails

def docket_number_update_dtotodb(
    existing_data: NocApplicationDetails, docket_number: str
) -> NocApplicationDetails:
    existing_data.docket_number = docket_number

    return existing_data
