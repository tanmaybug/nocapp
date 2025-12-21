from dtos.form1DTOcg import Form1
from helpers.dateHelper import date_time
from models.applicationDetailsModel import NocApplicationDetails

def dtotodb_insert(regId: str, client_ip: str) -> NocApplicationDetails:
    result = NocApplicationDetails(
        noc_registration_id = regId,
        insert_time = date_time(),
        insert_ip = client_ip,
        active_status = 1,
    )
    return result

def dtotodb(form_data: Form1,regId:str) -> NocApplicationDetails:
    result = NocApplicationDetails(
         # --- Identifiers ---
            noc_registration_id=regId,
            project_state_id_fk=45678,

            # --- Aim & Objective ---
            vision_for_college=form_data.aimAndObjective.vision if form_data.aimAndObjective else None,
            mission_for_college=form_data.aimAndObjective.mission if form_data.aimAndObjective else None,
            core_values_for_college=form_data.aimAndObjective.coreValues if form_data.aimAndObjective else None,
            aims_for_college=form_data.aimAndObjective.aims if form_data.aimAndObjective else None,
            objective_for_college=form_data.aimAndObjective.objectiveConcernedInstitution if form_data.aimAndObjective else None,

            # --- College Land Details ---
            college_land_mouza=form_data.collegeLandDetails.mouza if form_data.collegeLandDetails else None,
            college_land_jl=form_data.collegeLandDetails.jlNo if form_data.collegeLandDetails else None,
            college_land_khatian=form_data.collegeLandDetails.khatianNo if form_data.collegeLandDetails else None,
            college_land_plot_no=form_data.collegeLandDetails.plotNo if form_data.collegeLandDetails else None,
            college_area=str(form_data.collegeLandDetails.areaClasification) if form_data.collegeLandDetails else None,
            college_land_area_in_acre=form_data.collegeLandAreaInAcres,
            built_up_space_area=form_data.collegeCoveredArea,

            # --- Credibility & Readiness ---
            entity_experience_in_education_sector=form_data.credibilityAndReadiness.experienceInEducation if form_data.credibilityAndReadiness else None,
            entity_general_reputation=form_data.credibilityAndReadiness.generalReputation if form_data.credibilityAndReadiness else None,

            # --- Additional Commitments ---
            student_reservation_flag=form_data.additionalCommitmentsAndPlans.studentReservation if form_data.additionalCommitmentsAndPlans else None,
            employee_reservation_flag=form_data.additionalCommitmentsAndPlans.employeeReservation if form_data.additionalCommitmentsAndPlans else None,
            skill_development_activities_flag=form_data.additionalCommitmentsAndPlans.specialSkillDevelomentActivity if form_data.additionalCommitmentsAndPlans else None,
            academic_auditing_plan_flag=form_data.additionalCommitmentsAndPlans.academicAuditingPlans if form_data.additionalCommitmentsAndPlans else None,

            # --- Land Status ---
            land_owned_flag=form_data.landStatus.landOwnedStatus if form_data.landStatus else None,
            land_educational_purpose_flag=form_data.landStatus.landConvertedForEducationalPurposeStatus if form_data.landStatus else None,

            # --- Comprehensive Plan ---
            comprehensive_plan=form_data.comprehensivePlan,

            # --- Campus Development Plan ---
            total_build_up_area_for_building_plan=form_data.campusDevlopmentPlan.approvedPlanWith.totalBuildUpArea if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.approvedPlanWith else None,
            ground_floor_build_up_area=form_data.campusDevlopmentPlan.approvedPlanWith.groundFloorArea if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.approvedPlanWith else None,
            first_floor_build_up_area=form_data.campusDevlopmentPlan.approvedPlanWith.firstFloorArea if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.approvedPlanWith else None,

            total_classroom=form_data.campusDevlopmentPlan.totalNumberOf.classRoomCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.totalNumberOf else None,
            total_seminar_room=form_data.campusDevlopmentPlan.totalNumberOf.seminarRoomCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.totalNumberOf else None,
            total_multipurpose_hall=form_data.campusDevlopmentPlan.totalNumberOf.multipurposeHallCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.totalNumberOf else None,
            total_laboratories=form_data.campusDevlopmentPlan.totalNumberOf.labResourceCenterCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.totalNumberOf else None,
            total_educational_technology_lab=form_data.campusDevlopmentPlan.totalNumberOf.ictEduTechLabCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.totalNumberOf else None,
            total_language_lab=form_data.campusDevlopmentPlan.totalNumberOf.languageLabCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.totalNumberOf else None,
            total_store_room=form_data.campusDevlopmentPlan.totalNumberOf.storeRoomCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.totalNumberOf else None,
            boys_common_room_flag=form_data.campusDevlopmentPlan.totalNumberOf.boysCommonRoomCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.totalNumberOf else None,
            girls_common_room_flag=form_data.campusDevlopmentPlan.totalNumberOf.girlsCommonRoomCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.totalNumberOf else None,
            total_male_toilet=form_data.campusDevlopmentPlan.totalNumberOf.boysToiletCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.totalNumberOf else None,
            total_female_toilet=form_data.campusDevlopmentPlan.totalNumberOf.girlsToiletCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.totalNumberOf else None,
            administrative_office_flag=form_data.campusDevlopmentPlan.administrativeOfficeStatus if form_data.campusDevlopmentPlan else None,

            conference_room_flag=form_data.campusDevlopmentPlan.anyOtherRoom.conferrenceRoomStatus if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.anyOtherRoom else None,
            meeting_room_flag=form_data.campusDevlopmentPlan.anyOtherRoom.meetingRoomStatus if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.anyOtherRoom else None,

            library_space=form_data.campusDevlopmentPlan.libraryDetails.totalSpace if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.libraryDetails else None,
            library_reading_rooms_count=form_data.campusDevlopmentPlan.libraryDetails.readingRoomCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.libraryDetails else None,
            library_books_count=form_data.campusDevlopmentPlan.libraryDetails.booksCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.libraryDetails else None,
            library_journal_count=form_data.campusDevlopmentPlan.libraryDetails.journalPeriodicalCount if form_data.campusDevlopmentPlan and form_data.campusDevlopmentPlan.libraryDetails else None,
            total_planned_construction_in_sq_feet=form_data.campusDevlopmentPlan.totalPlannedConstruction if form_data.campusDevlopmentPlan else None,
    )
    return result
