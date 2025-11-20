from config.DB.DBConfig import Base
from sqlalchemy import Column, Integer, Float, String, Text, SmallInteger, Date, TIMESTAMP
from sqlalchemy.sql import func

class NocApplicationDetails(Base):
    __tablename__ = "noc_application_details"

    noc_registration_id = Column(String(255), primary_key=True, index=True)
    project_state_id_fk = Column(Integer)

    vision_for_college = Column(Text)
    mission_for_college = Column(Text)
    core_values_for_college = Column(Text)
    aims_for_college = Column(Text)
    objective_for_college = Column(Text)

    college_land_mouza = Column(Text)
    college_land_jl = Column(Text)
    college_land_khatian = Column(Text)
    college_land_plot_no = Column(String(255))
    college_area = Column(String(255))
    college_land_area_in_acre = Column(Float)
    built_up_space_area = Column(Float)

    entity_experience_in_education_sector = Column(Text)
    entity_general_reputation = Column(Text)

    student_reservation_flag = Column(SmallInteger)
    employee_reservation_flag = Column(SmallInteger)
    skill_development_activities_flag = Column(SmallInteger)
    academic_auditing_plan_flag = Column(SmallInteger)

    land_owned_flag = Column(SmallInteger)
    land_educational_purpose_flag = Column(SmallInteger)

    comprehensive_plan = Column(Text)

    total_build_up_area_for_building_plan = Column(Float)
    ground_floor_build_up_area = Column(Float)
    first_floor_build_up_area = Column(Float)

    total_classroom = Column(SmallInteger)
    total_seminar_room = Column(SmallInteger)
    total_multipurpose_hall = Column(SmallInteger)
    total_laboratories = Column(SmallInteger)
    total_educational_technology_lab = Column(SmallInteger)
    total_language_lab = Column(SmallInteger)
    total_store_room = Column(SmallInteger)
    boys_common_room_flag = Column(SmallInteger)
    girls_common_room_flag = Column(SmallInteger)
    administrative_office_flag = Column(SmallInteger)
    total_male_toilet = Column(SmallInteger)
    total_female_toilet = Column(SmallInteger)
    conference_room_flag = Column(SmallInteger)
    meeting_room_flag = Column(SmallInteger)

    library_space = Column(SmallInteger)
    library_reading_rooms_count = Column(SmallInteger)
    library_books_count = Column(Integer)
    library_journal_count = Column(Integer)

    total_planned_construction_in_sq_feet = Column(Float)
    source_fund_amount = Column(Float)
    source_of_fund = Column(Text)
    proposed_investment_amount = Column(Float)
    proposed_employment_count = Column(Integer)
    total_planned_construction_area = Column(Float)
    nearby_professional_colleges_count = Column(SmallInteger)
    nearby_feeder_school_count = Column(SmallInteger)

    date_of_completion_flag = Column(SmallInteger)
    date_of_completion_building = Column(Date)

    insert_time = Column(TIMESTAMP, server_default=func.now())
    insert_ip = Column(String(15))
    active_status = Column(SmallInteger, default=1)
