from dtos.form1DTOcg import (AdditionalCommitmentsAndPlans, AimAndObjective, AnyOtherRoom, ApprovedPlanWith, CampusDevelopmentPlan, CollegeLandDetails, CredibilityAndReadiness, Form1, LandStatus, LibraryDetails, TotalNumberOf)
from helpers.dateHelper import date_time
from models.applicationDetailsModel import NocApplicationDetails
# from fastapi.encoders import jsonable_encoder
from typing import Any, Dict

def dtotodb_insert(regId: str, client_ip: str) -> NocApplicationDetails:
    result = NocApplicationDetails(
        noc_registration_id=regId,
        application_status=1,
        insert_time=date_time(),
        insert_ip=client_ip,
        active_status=1,
    )
    return result

def dtotodb_update(form_data: Form1, existing_obj: NocApplicationDetails) -> NocApplicationDetails:
    """
    Updates an existing NocApplicationDetails object with Form1 data.
    Only updates fields present in the DTO; preserves other existing fields.
    """

    application = existing_obj.NocApplicationDetails
    # print(f"form data : {application}")

    # --- Aim & Objective ---
    if form_data.aimAndObjective:
        if form_data.aimAndObjective.vision is not None:
            application.vision_for_college = form_data.aimAndObjective.vision
        if form_data.aimAndObjective.mission is not None:
            application.mission_for_college = form_data.aimAndObjective.mission
        if form_data.aimAndObjective.coreValues is not None:
            application.core_values_for_college = form_data.aimAndObjective.coreValues
        if form_data.aimAndObjective.aims is not None:
            application.aims_for_college = form_data.aimAndObjective.aims
        if form_data.aimAndObjective.objectiveConcernedInstitution is not None:
            application.objective_for_college = (
                form_data.aimAndObjective.objectiveConcernedInstitution
            )

    # --- College Land Details ---
    if form_data.collegeLandDetails:
        if form_data.collegeLandDetails.mouza is not None:
            application.college_land_mouza = form_data.collegeLandDetails.mouza
        if form_data.collegeLandDetails.jlNo is not None:
            application.college_land_jl = form_data.collegeLandDetails.jlNo
        if form_data.collegeLandDetails.khatianNo is not None:
            application.college_land_khatian = form_data.collegeLandDetails.khatianNo
        if form_data.collegeLandDetails.plotNo is not None:
            application.college_land_plot_no = form_data.collegeLandDetails.plotNo
        if form_data.collegeLandDetails.areaClasification is not None:
            application.college_area = str(
                form_data.collegeLandDetails.areaClasification
            )

    if form_data.collegeLandAreaInAcres is not None:
        application.college_land_area_in_acre = form_data.collegeLandAreaInAcres
    if form_data.collegeCoveredArea is not None:
        application.built_up_space_area = form_data.collegeCoveredArea

    # --- Credibility & Readiness ---
    if form_data.credibilityAndReadiness:
        if form_data.credibilityAndReadiness.experienceInEducation is not None:
            application.entity_experience_in_education_sector = (
                form_data.credibilityAndReadiness.experienceInEducation
            )
        if form_data.credibilityAndReadiness.generalReputation is not None:
            application.entity_general_reputation = (
                form_data.credibilityAndReadiness.generalReputation
            )

    # --- Additional Commitments ---
    if form_data.additionalCommitmentsAndPlans:
        if form_data.additionalCommitmentsAndPlans.studentReservation is not None:
            application.student_reservation_flag = (
                form_data.additionalCommitmentsAndPlans.studentReservation
            )
        if form_data.additionalCommitmentsAndPlans.employeeReservation is not None:
            application.employee_reservation_flag = (
                form_data.additionalCommitmentsAndPlans.employeeReservation
            )
        if form_data.additionalCommitmentsAndPlans.specialSkillDevelomentActivity is not None:
            application.skill_development_activities_flag = (
                form_data.additionalCommitmentsAndPlans.specialSkillDevelomentActivity
            )
        if form_data.additionalCommitmentsAndPlans.academicAuditingPlans is not None:
            application.academic_auditing_plan_flag = (
                form_data.additionalCommitmentsAndPlans.academicAuditingPlans
            )

    # --- Land Status ---
    if form_data.landStatus:
        if form_data.landStatus.landOwnedStatus is not None:
            application.land_owned_flag = form_data.landStatus.landOwnedStatus
        if form_data.landStatus.landConvertedForEducationalPurposeStatus is not None:
            application.land_educational_purpose_flag = (
                form_data.landStatus.landConvertedForEducationalPurposeStatus
            )

    # --- Comprehensive Plan ---
    if form_data.comprehensivePlan is not None:
        application.comprehensive_plan = form_data.comprehensivePlan

    # --- Campus Development Plan ---
    if form_data.campusDevlopmentPlan:

        if form_data.campusDevlopmentPlan.approvedPlanWith:
            if form_data.campusDevlopmentPlan.approvedPlanWith.totalBuildUpArea is not None:
                application.total_build_up_area_for_building_plan = (
                    form_data.campusDevlopmentPlan.approvedPlanWith.totalBuildUpArea
                )
            if form_data.campusDevlopmentPlan.approvedPlanWith.groundFloorArea is not None:
                application.ground_floor_build_up_area = (
                    form_data.campusDevlopmentPlan.approvedPlanWith.groundFloorArea
                )
            if form_data.campusDevlopmentPlan.approvedPlanWith.firstFloorArea is not None:
                application.first_floor_build_up_area = (
                    form_data.campusDevlopmentPlan.approvedPlanWith.firstFloorArea
                )

        if form_data.campusDevlopmentPlan.totalNumberOf:
            tno = form_data.campusDevlopmentPlan.totalNumberOf

            if tno.classRoomCount is not None:
                application.total_classroom = tno.classRoomCount
            if tno.seminarRoomCount is not None:
                application.total_seminar_room = tno.seminarRoomCount
            if tno.multipurposeHallCount is not None:
                application.total_multipurpose_hall = tno.multipurposeHallCount
            if tno.labResourceCenterCount is not None:
                application.total_laboratories = tno.labResourceCenterCount
            if tno.ictEduTechLabCount is not None:
                application.total_educational_technology_lab = tno.ictEduTechLabCount
            if tno.languageLabCount is not None:
                application.total_language_lab = tno.languageLabCount
            if tno.storeRoomCount is not None:
                application.total_store_room = tno.storeRoomCount
            if tno.boysCommonRoomCount is not None:
                application.boys_common_room_flag = tno.boysCommonRoomCount
            if tno.girlsCommonRoomCount is not None:
                application.girls_common_room_flag = tno.girlsCommonRoomCount
            if tno.boysToiletCount is not None:
                application.total_male_toilet = tno.boysToiletCount
            if tno.girlsToiletCount is not None:
                application.total_female_toilet = tno.girlsToiletCount

        if form_data.campusDevlopmentPlan.administrativeOfficeStatus is not None:
            application.administrative_office_flag = (
                form_data.campusDevlopmentPlan.administrativeOfficeStatus
            )

        if form_data.campusDevlopmentPlan.anyOtherRoom:
            if form_data.campusDevlopmentPlan.anyOtherRoom.conferrenceRoomStatus is not None:
                application.conference_room_flag = (
                    form_data.campusDevlopmentPlan.anyOtherRoom.conferrenceRoomStatus
                )
            if form_data.campusDevlopmentPlan.anyOtherRoom.meetingRoomStatus is not None:
                application.meeting_room_flag = (
                    form_data.campusDevlopmentPlan.anyOtherRoom.meetingRoomStatus
                )

        if form_data.campusDevlopmentPlan.libraryDetails:
            if form_data.campusDevlopmentPlan.libraryDetails.totalSpace is not None:
                application.library_space = (
                    form_data.campusDevlopmentPlan.libraryDetails.totalSpace
                )
            if form_data.campusDevlopmentPlan.libraryDetails.readingRoomCount is not None:
                application.library_reading_rooms_count = (
                    form_data.campusDevlopmentPlan.libraryDetails.readingRoomCount
                )
            if form_data.campusDevlopmentPlan.libraryDetails.booksCount is not None:
                application.library_books_count = (
                    form_data.campusDevlopmentPlan.libraryDetails.booksCount
                )
            if form_data.campusDevlopmentPlan.libraryDetails.journalPeriodicalCount is not None:
                application.library_journal_count = (
                    form_data.campusDevlopmentPlan.libraryDetails.journalPeriodicalCount
                )

        if form_data.campusDevlopmentPlan.totalPlannedConstruction is not None:
            application.total_planned_construction_in_sq_feet = (
                form_data.campusDevlopmentPlan.totalPlannedConstruction
            )

    return application


def dbtodto(db: Dict[str, Any]) -> Form1:
    # db = data.get("NocApplicationDetails", {})

    return Form1(
        aimAndObjective=AimAndObjective(
            vision=db.get("vision_for_college"),
            mission=db.get("mission_for_college"),
            coreValues=db.get("core_values_for_college"),
            aims=db.get("aims_for_college"),
            objectiveConcernedInstitution=db.get("objective_for_college"),
        ),

        collegeLandDetails=CollegeLandDetails(
            mouza=db.get("college_land_mouza"),
            jlNo=db.get("college_land_jl"),
            khatianNo=db.get("college_land_khatian"),
            plotNo=db.get("college_land_plot_no"),
            areaClasification=db.get("area_classification"),
        ),

        credibilityAndReadiness=CredibilityAndReadiness(
            experienceInEducation=db.get(
                "entity_experience_in_education_sector"
            ),
            generalReputation=db.get("entity_general_reputation"),
            readinessToComplyWithRegulatoryNorms=db.get(
                "readiness_to_comply_with_regulatory_norms"
            ),
        ),

        additionalCommitmentsAndPlans=AdditionalCommitmentsAndPlans(
            studentReservation=db.get("student_reservation_flag"),
            employeeReservation=db.get("employee_reservation_flag"),
            specialSkillDevelomentActivity=db.get(
                "skill_development_activities_flag"
            ),
            academicAuditingPlans=db.get(
                "academic_auditing_plan_flag"
            ),
        ),

        campusDevlopmentPlan=CampusDevelopmentPlan(
            approvedPlanWith=ApprovedPlanWith(
                totalBuildUpArea=db.get(
                    "total_build_up_area_for_building_plan"
                ),
                groundFloorArea=db.get(
                    "ground_floor_build_up_area"
                ),
                firstFloorArea=db.get(
                    "first_floor_build_up_area"
                ),
            ),

            totalNumberOf=TotalNumberOf(
                classRoomCount=db.get("total_classroom"),
                seminarRoomCount=db.get("total_seminar_room"),
                multipurposeHallCount=db.get(
                    "total_multipurpose_hall"
                ),
                labResourceCenterCount=db.get(
                    "total_laboratories"
                ),
                ictEduTechLabCount=db.get(
                    "total_educational_technology_lab"
                ),
                languageLabCount=db.get("total_language_lab"),
                storeRoomCount=db.get("total_store_room"),
                boysCommonRoomCount=db.get(
                    "boys_common_room_flag"
                ),
                girlsCommonRoomCount=db.get(
                    "girls_common_room_flag"
                ),
                boysToiletCount=db.get("total_male_toilet"),
                girlsToiletCount=db.get("total_female_toilet"),
            ),

            anyOtherRoom=AnyOtherRoom(
                conferrenceRoomStatus=db.get(
                    "conference_room_flag"
                ),
                meetingRoomStatus=db.get("meeting_room_flag"),
            ),

            libraryDetails=LibraryDetails(
                totalSpace=db.get("library_space"),
                readingRoomCount=db.get(
                    "library_reading_rooms_count"
                ),
                booksCount=db.get("library_books_count"),
                journalPeriodicalCount=db.get(
                    "library_journal_count"
                ),
            ),

            administrativeOfficeStatus=db.get(
                "administrative_office_flag"
            ),

            totalPlannedConstruction=db.get(
                "total_planned_construction_in_sq_feet"
            ),
        ),

        comprehensivePlan=db.get("comprehensive_plan"),

        collegeLandAreaInAcres=db.get(
            "college_land_area_in_acre"
        ),

        collegeCoveredArea=db.get("college_area"),

        landStatus=LandStatus(
            landOwnedStatus=db.get("land_owned_flag"),

            landConvertedForEducationalPurposeStatus=db.get(
                "land_educational_purpose_flag"
            ),
        ),
    )
