from dtos.department.reportResponseDTO import (
    ApplicationListReport,
    CollegeProfile,
    CollegeInfrastructure,
)

def applicant_report_dbtodto(db_data):
    response = []
    for row in db_data:
        # data = row["NocApplicationDetails"]

        response.append(
            ApplicationListReport(
                registrationId=row["noc_registration_id"],
                institutionName=row["institute_name"],
                applicantName=row["applicant_name"],
                applicantPhone=row["applicant_mobile"],
                applicantEmail=row["applicant_email_id"],
            )
        )
    return response

def transform_noc_data(db_rows):
    response = []

    for row in db_rows:
        data = row["NocApplicationDetails"]

        response.append(
            CollegeProfile(
                objective=data["objective_for_college"],
                experience=data["entity_experience_in_education_sector"],
                reputation=data["entity_general_reputation"],
                development_plan=data["comprehensive_plan"],
                funding_source=data["source_of_fund"],
                land_mouza=data["college_land_mouza"],
                created_at=data["insert_time"],
                infrastructure=CollegeInfrastructure(
                    ed_tech_labs=data["total_educational_technology_lab"],
                    language_labs=data["total_language_lab"],
                    conference_room=bool(data["conference_room_flag"]),
                    meeting_room=bool(data["meeting_room_flag"]),
                    built_up_area_sqft=data["total_build_up_area_for_building_plan"],
                ),
            )
        )

    return response
