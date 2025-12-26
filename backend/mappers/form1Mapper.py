from dtos.form1DTOcg import Form1
from helpers.dateHelper import date_time
from models.applicationDetailsModel import NocApplicationDetails

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

    # --- Aim & Objective ---
    if form_data.aimAndObjective:
        if form_data.aimAndObjective.vision is not None:
            existing_obj.vision_for_college = form_data.aimAndObjective.vision
        if form_data.aimAndObjective.mission is not None:
            existing_obj.mission_for_college = form_data.aimAndObjective.mission
        if form_data.aimAndObjective.coreValues is not None:
            existing_obj.core_values_for_college = form_data.aimAndObjective.coreValues
        if form_data.aimAndObjective.aims is not None:
            existing_obj.aims_for_college = form_data.aimAndObjective.aims
        if form_data.aimAndObjective.objectiveConcernedInstitution is not None:
            existing_obj.objective_for_college = (
                form_data.aimAndObjective.objectiveConcernedInstitution
            )

    # --- College Land Details ---
    if form_data.collegeLandDetails:
        if form_data.collegeLandDetails.mouza is not None:
            existing_obj.college_land_mouza = form_data.collegeLandDetails.mouza
        if form_data.collegeLandDetails.jlNo is not None:
            existing_obj.college_land_jl = form_data.collegeLandDetails.jlNo
        if form_data.collegeLandDetails.khatianNo is not None:
            existing_obj.college_land_khatian = form_data.collegeLandDetails.khatianNo
        if form_data.collegeLandDetails.plotNo is not None:
            existing_obj.college_land_plot_no = form_data.collegeLandDetails.plotNo
        if form_data.collegeLandDetails.areaClasification is not None:
            existing_obj.college_area = str(
                form_data.collegeLandDetails.areaClasification
            )

    if form_data.collegeLandAreaInAcres is not None:
        existing_obj.college_land_area_in_acre = form_data.collegeLandAreaInAcres
    if form_data.collegeCoveredArea is not None:
        existing_obj.built_up_space_area = form_data.collegeCoveredArea

    # --- Credibility & Readiness ---
    if form_data.credibilityAndReadiness:
        if form_data.credibilityAndReadiness.experienceInEducation is not None:
            existing_obj.entity_experience_in_education_sector = (
                form_data.credibilityAndReadiness.experienceInEducation
            )
        if form_data.credibilityAndReadiness.generalReputation is not None:
            existing_obj.entity_general_reputation = (
                form_data.credibilityAndReadiness.generalReputation
            )

    # --- Additional Commitments ---
    if form_data.additionalCommitmentsAndPlans:
        if form_data.additionalCommitmentsAndPlans.studentReservation is not None:
            existing_obj.student_reservation_flag = (
                form_data.additionalCommitmentsAndPlans.studentReservation
            )
        if form_data.additionalCommitmentsAndPlans.employeeReservation is not None:
            existing_obj.employee_reservation_flag = (
                form_data.additionalCommitmentsAndPlans.employeeReservation
            )
        if form_data.additionalCommitmentsAndPlans.specialSkillDevelomentActivity is not None:
            existing_obj.skill_development_activities_flag = (
                form_data.additionalCommitmentsAndPlans.specialSkillDevelomentActivity
            )
        if form_data.additionalCommitmentsAndPlans.academicAuditingPlans is not None:
            existing_obj.academic_auditing_plan_flag = (
                form_data.additionalCommitmentsAndPlans.academicAuditingPlans
            )

    # --- Land Status ---
    if form_data.landStatus:
        if form_data.landStatus.landOwnedStatus is not None:
            existing_obj.land_owned_flag = form_data.landStatus.landOwnedStatus
        if form_data.landStatus.landConvertedForEducationalPurposeStatus is not None:
            existing_obj.land_educational_purpose_flag = (
                form_data.landStatus.landConvertedForEducationalPurposeStatus
            )

    # --- Comprehensive Plan ---
    if form_data.comprehensivePlan is not None:
        existing_obj.comprehensive_plan = form_data.comprehensivePlan

    # --- Campus Development Plan ---
    if form_data.campusDevlopmentPlan:

        if form_data.campusDevlopmentPlan.approvedPlanWith:
            if form_data.campusDevlopmentPlan.approvedPlanWith.totalBuildUpArea is not None:
                existing_obj.total_build_up_area_for_building_plan = (
                    form_data.campusDevlopmentPlan.approvedPlanWith.totalBuildUpArea
                )
            if form_data.campusDevlopmentPlan.approvedPlanWith.groundFloorArea is not None:
                existing_obj.ground_floor_build_up_area = (
                    form_data.campusDevlopmentPlan.approvedPlanWith.groundFloorArea
                )
            if form_data.campusDevlopmentPlan.approvedPlanWith.firstFloorArea is not None:
                existing_obj.first_floor_build_up_area = (
                    form_data.campusDevlopmentPlan.approvedPlanWith.firstFloorArea
                )

        if form_data.campusDevlopmentPlan.totalNumberOf:
            tno = form_data.campusDevlopmentPlan.totalNumberOf

            if tno.classRoomCount is not None:
                existing_obj.total_classroom = tno.classRoomCount
            if tno.seminarRoomCount is not None:
                existing_obj.total_seminar_room = tno.seminarRoomCount
            if tno.multipurposeHallCount is not None:
                existing_obj.total_multipurpose_hall = tno.multipurposeHallCount
            if tno.labResourceCenterCount is not None:
                existing_obj.total_laboratories = tno.labResourceCenterCount
            if tno.ictEduTechLabCount is not None:
                existing_obj.total_educational_technology_lab = tno.ictEduTechLabCount
            if tno.languageLabCount is not None:
                existing_obj.total_language_lab = tno.languageLabCount
            if tno.storeRoomCount is not None:
                existing_obj.total_store_room = tno.storeRoomCount
            if tno.boysCommonRoomCount is not None:
                existing_obj.boys_common_room_flag = tno.boysCommonRoomCount
            if tno.girlsCommonRoomCount is not None:
                existing_obj.girls_common_room_flag = tno.girlsCommonRoomCount
            if tno.boysToiletCount is not None:
                existing_obj.total_male_toilet = tno.boysToiletCount
            if tno.girlsToiletCount is not None:
                existing_obj.total_female_toilet = tno.girlsToiletCount

        if form_data.campusDevlopmentPlan.administrativeOfficeStatus is not None:
            existing_obj.administrative_office_flag = (
                form_data.campusDevlopmentPlan.administrativeOfficeStatus
            )

        if form_data.campusDevlopmentPlan.anyOtherRoom:
            if form_data.campusDevlopmentPlan.anyOtherRoom.conferrenceRoomStatus is not None:
                existing_obj.conference_room_flag = (
                    form_data.campusDevlopmentPlan.anyOtherRoom.conferrenceRoomStatus
                )
            if form_data.campusDevlopmentPlan.anyOtherRoom.meetingRoomStatus is not None:
                existing_obj.meeting_room_flag = (
                    form_data.campusDevlopmentPlan.anyOtherRoom.meetingRoomStatus
                )

        if form_data.campusDevlopmentPlan.libraryDetails:
            if form_data.campusDevlopmentPlan.libraryDetails.totalSpace is not None:
                existing_obj.library_space = (
                    form_data.campusDevlopmentPlan.libraryDetails.totalSpace
                )
            if form_data.campusDevlopmentPlan.libraryDetails.readingRoomCount is not None:
                existing_obj.library_reading_rooms_count = (
                    form_data.campusDevlopmentPlan.libraryDetails.readingRoomCount
                )
            if form_data.campusDevlopmentPlan.libraryDetails.booksCount is not None:
                existing_obj.library_books_count = (
                    form_data.campusDevlopmentPlan.libraryDetails.booksCount
                )
            if form_data.campusDevlopmentPlan.libraryDetails.journalPeriodicalCount is not None:
                existing_obj.library_journal_count = (
                    form_data.campusDevlopmentPlan.libraryDetails.journalPeriodicalCount
                )

        if form_data.campusDevlopmentPlan.totalPlannedConstruction is not None:
            existing_obj.total_planned_construction_in_sq_feet = (
                form_data.campusDevlopmentPlan.totalPlannedConstruction
            )

    return existing_obj


def dbtodto(db: NocApplicationDetails) -> Form1:
    return Form1(

        # --- Aim & Objective ---
        vision=db.vision_for_college,
        mission=db.mission_for_college,
        coreValues=db.core_values_for_college,
        aims=db.aims_for_college,
        objectiveConcernedInstitution=db.objective_for_college,

        # --- College Land Details ---
        mouza=db.college_land_mouza,
        jlNo=db.college_land_jl,
        khatianNo=db.college_land_khatian,
        plotNo=db.college_land_plot_no,
        areaClasification=db.college_area,
        collegeLandAreaInAcres=db.college_land_area_in_acre,
        collegeCoveredArea=db.built_up_space_area,

        # --- Credibility & Readiness ---
        experienceInEducation=db.entity_experience_in_education_sector,
        generalReputation=db.entity_general_reputation,

        # --- Additional Commitments ---
        studentReservation=db.student_reservation_flag,
        employeeReservation=db.employee_reservation_flag,
        specialSkillDevelomentActivity=db.skill_development_activities_flag,
        academicAuditingPlans=db.academic_auditing_plan_flag,

        # --- Land Status ---
        landOwnedStatus=db.land_owned_flag,
        landConvertedForEducationalPurposeStatus=db.land_educational_purpose_flag,

        # --- Comprehensive Plan ---
        comprehensivePlan=db.comprehensive_plan,

        # --- Campus Development Plan ---
        totalBuildUpArea=db.total_build_up_area_for_building_plan,
        groundFloorArea=db.ground_floor_build_up_area,
        firstFloorArea=db.first_floor_build_up_area,

        classRoomCount=db.total_classroom,
        seminarRoomCount=db.total_seminar_room,
        multipurposeHallCount=db.total_multipurpose_hall,
        labResourceCenterCount=db.total_laboratories,
        ictEduTechLabCount=db.total_educational_technology_lab,
        languageLabCount=db.total_language_lab,
        storeRoomCount=db.total_store_room,
        boysCommonRoomCount=db.boys_common_room_flag,
        girlsCommonRoomCount=db.girls_common_room_flag,
        boysToiletCount=db.total_male_toilet,
        girlsToiletCount=db.total_female_toilet,

        administrativeOfficeStatus=db.administrative_office_flag,
        conferrenceRoomStatus=db.conference_room_flag,
        meetingRoomStatus=db.meeting_room_flag,

        libraryTotalSpace=db.library_space,
        libraryReadingRoomCount=db.library_reading_rooms_count,
        libraryBooksCount=db.library_books_count,
        libraryJournalPeriodicalCount=db.library_journal_count,

        totalPlannedConstruction=db.total_planned_construction_in_sq_feet,
    )
