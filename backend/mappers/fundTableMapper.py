from helpers.dateHelper import date_time
from models.fundTableModel import FundUtilization

def dtotodb(data, regID:str) -> FundUtilization:
    result = []
    for item_data in data:
        db_item = FundUtilization(
            noc_registration_id=regID,
            financial_resources_year=item_data.year,
            financial_resources_fund=item_data.source,
            financial_resources_utilisation=item_data.utilisation,
            active_status=1,
            fund_resources_entry_time=date_time(),
            fund_resources_entry_ip="127.0.0.1",
        )
        result.append(db_item)

    return result
