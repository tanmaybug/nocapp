from dtos.form2DTO import Form2, ProjectedFundFlow, Synopsis
from models.applicationDetailsModel import NocApplicationDetails
from typing import Any, Dict


def updatedb(form_data: Form2, existing_obj: NocApplicationDetails) -> NocApplicationDetails:
    """
    Updates an existing NocApplicationDetails object with Form2 data.
    Only updates fields present in the DTO; preserves other existing fields.
    """

    application = existing_obj.NocApplicationDetails

    # --- Projected Fund Flow ---
    if form_data.projectedFundFlow:
        if form_data.projectedFundFlow.amount is not None:
            application.source_fund_amount = form_data.projectedFundFlow.amount
        if form_data.projectedFundFlow.sourceOfFund is not None:
            application.source_of_fund = form_data.projectedFundFlow.sourceOfFund

    # --- Synopsis ---
    if form_data.synopsis:
        if form_data.synopsis.proposedInvestment is not None:
            application.proposed_investment_amount = form_data.synopsis.proposedInvestment
        if form_data.synopsis.proposedEmployment is not None:
            application.proposed_employment_count = int(form_data.synopsis.proposedEmployment)
        if form_data.synopsis.professionalCollegesCountWithin25Km is not None:
            application.nearby_professional_colleges_count = form_data.synopsis.professionalCollegesCountWithin25Km
        if form_data.synopsis.feederSchoolCountWithin15Km is not None:
            application.nearby_feeder_school_count = form_data.synopsis.feederSchoolCountWithin15Km

    # --- Building Details ---
    # if form_data.buildingDetails:
    #     if form_data.buildingDetails.buildingCompletionStatus is not None:
    #         application.date_of_completion_flag = form_data.buildingDetails.buildingCompletionStatus
    #     if form_data.buildingDetails.buildingCompletionDate is not None:
    #         application.date_of_completion_building = form_data.buildingDetails.buildingCompletionDate

    if form_data.buildingCompletionStatus is not None:
        application.date_of_completion_flag = form_data.buildingCompletionStatus
    if form_data.buildingCompletionDate is not None:
        application.date_of_completion_building = form_data.buildingCompletionDate

    # if form_data.buildingCompletionExpectedDate is not None:
    #     application.date_of_completion_building = form_data.buildingCompletionExpectedDate
    # if form_data.buildingPlanAmountToBeDeposited is not None:
    #     application.date_of_completion_building = form_data.buildingPlanAmountToBeDeposited
    # if form_data.estimatedIncomeAndExpenditureForFirst5Years is not None:
    #     application.date_of_completion_building = form_data.estimatedIncomeAndExpenditureForFirst5Years
    # if form_data.initialFundInformation is not None:
    #     application.date_of_completion_building = form_data.initialFundInformation
    # if form_data.nationalizedBank is not None:
    #     application.date_of_completion_building = form_data.nationalizedBank
    
    
    return application


def dbtodto(data: Dict[str, Any]) -> Form2:
    return Form2(
        projectedFundFlow=ProjectedFundFlow(
            amount=data.get("source_fund_amount"),
            sourceOfFund=data.get("source_of_fund"),
        ),
        synopsis=Synopsis(
            proposedInvestment=data.get("proposed_investment_amount"),
            proposedEmployment=data.get("proposed_employment_count"),
            professionalCollegesCountWithin25Km=data.get(
                "nearby_professional_colleges_count"
            ),
            feederSchoolCountWithin15Km=data.get("nearby_feeder_school_count"),
        ),
        buildingCompletionStatus=data.get("date_of_completion_flag"),
        buildingCompletionDate=data.get("date_of_completion_building"),
        buildingCompletionExpectedDate=None,
        buildingPlanAmountToBeDeposited=None,
        estimatedIncomeAndExpenditureForFirst5Years=None,
        initialFundInformation=None,
        nationalizedBank=None
    )