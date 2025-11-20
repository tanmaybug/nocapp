from dtos.registrationFormDTO import RegistrationFormRequestDTO
from helpers.dateHelper import date_time
from models.NOCRegistrationTableModel import NOCRegistration


def dbtodto(data: NOCRegistration):
    pass


def dtotodb(data: RegistrationFormRequestDTO,regId:str) -> NOCRegistration:
    result = NOCRegistration(
        applicant_type_id_fk=data.entityTypeID,
        applicant_name=data.applicantName,
        socities_rigistration_act_flag=data.isRegistered,
        minority_type_id_fk=data.minorityTypeId,
        minority_flag=data.minorityFlag,
        registration_no=data.registrationNo,
        registration_date=data.registrationDate,
        registration_place=data.placeOfRegistration,
        details_minority_status=data.minorityDetails,
        applicant_address=data.applicantLocation.applicantAddress,
        applicant_dst_id_fk=data.applicantLocation.districtId,
        applicant_subdiv_id_fk=data.applicantLocation.subDivisionId,
        applicant_police_station_id_fk=data.applicantLocation.policeStationId,
        applicant_post_office_id_fk=data.applicantLocation.postOfficeId,
        applicant_block_mun_id_fk=data.applicantLocation.municipalityBlockId,
        applicant_assembly_constitution_id_fk=data.applicantLocation.assemblyConstituencyId,
        applicant_city=data.applicantLocation.city,
        applicant_pin=data.applicantLocation.pin,
        institute_name=data.proposedCollegeName,
        aff_unv_id_fk=data.affiliatedUniversityId,
        inst_type_id_fk=data.institutionForId,
        institution_address=data.collegeLocation.college_address,
        institution_dst_id_fk=data.collegeLocation.districtId,
        institution_subdi_id_fk=data.collegeLocation.subDivisionId,
        institution_police_station_id_fk=data.collegeLocation.policeStationId,
        institution_post_office_id_fk=data.collegeLocation.postOfficeId,
        institution_panchayat_id_fk=data.collegeLocation.gramPanchayatId,
        institution_assembly_constitution_id_fk=data.collegeLocation.assemblyConstituencyId,
        institution_block_id_fk=data.collegeLocation.municipalityBlockId,
        institution_pin=data.collegeLocation.pin,
        noc_registration_id=regId,
        entry_time=date_time(),
        entry_ip="127.0.0.1",
        active_status=1,
    )

    return result
