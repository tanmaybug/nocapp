from fastapi import APIRouter, status, Depends, HTTPException
from dtos.registrationFormDTO import RegistrationFormRequestDTO
from helpers import response
from config.DB.DBConfig import get_db
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from mappers.registrationTableMapper import dtotodb as registrationMap
from mappers.form1Mapper import dtotodb_insert as form1Map
from mappers.loginTableMapper import dtotodb as loginMap
from mappers.applicationTrackMapper import dtotodb as applicationTrackMap
from utils.iP import get_client_ip
from utils.password import hash_password
from datetime import datetime

from services.applicantRegistrationRepo import applicantRegistrationService
from services.applicantTypeRepo import applicantTypeService
from services.institutionTypeMasterRepo import institutionTypeMasterService
from services.minorityTypeMasterRepo import minorityTypeService
from services.districtMasterRepo import districtMasterService
from services.subdivisionMasterRepo import subDevisionMasterService
from services.assemblyConstituencyMasterRepo import assemblyConstituencyService
from services.municipalityBlockMasterRepo import municipalityService
from services.policeStationMasterRepo import policeStationMasterService
from services.affiliatedUniversityRepo import affiliatedUniversityMasterService
from services.gramPanchyatMasterRepo import gramPanchyatService
from services.postOfficeMasterRepo import postOfficeMasterService

router = APIRouter(prefix="/registration", tags=["Registration"])

@router.get("", response_model=response.APIResponse)
def get_registration_master_data(db: Session = Depends(get_db)):

    noc_applicant_type = jsonable_encoder(applicantTypeService(db).get_data())
    minority_type = jsonable_encoder(minorityTypeService(db).get_data())
    noc_district = jsonable_encoder(districtMasterService(db).get_data())
    noc_subdiv = jsonable_encoder(subDevisionMasterService(db).get_data())
    noc_assembly_constituency = jsonable_encoder(
        assemblyConstituencyService(db).get_data()
    )
    noc_municipality_block = jsonable_encoder(municipalityService(db).get_data())
    police_station = jsonable_encoder(policeStationMasterService(db).get_data())
    aff_university = jsonable_encoder(affiliatedUniversityMasterService(db).get_data())
    institute_type = jsonable_encoder(institutionTypeMasterService(db).get_data())

    data = {
        "entityTypes": noc_applicant_type,
        "minorityTypes": minority_type,
        "districts": noc_district,
        "subDivisions": noc_subdiv,
        "assemblyConstituencies": noc_assembly_constituency,
        "municipalityBlocks": noc_municipality_block,
        "policeStations": police_station,
        "affiliatedUniversities": aff_university,
        "instituteType": institute_type,
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Master Data For Registration",
        "data": data,
    }
    return result


@router.get("/grampanchayats/{blockId}", response_model=response.APIResponse)
def get_grampanchayats(blockId:int,db: Session = Depends(get_db)):
    noc_gram_panchayat = jsonable_encoder(
        gramPanchyatService(db).get_data_by_blockid(blockId)
    )

    data = {
        "gramPanchayats": noc_gram_panchayat,
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Gram Panchayats For Registration",
        "data": data,
    }
    return result

@router.get("/postOffices/{pin}", response_model=response.APIResponse)
def get_postOffices(pin: int, db: Session = Depends(get_db)):
    noc_post_office = jsonable_encoder(postOfficeMasterService(db).get_data_by_pin_code(pin))

    data = {
        "postOffices": noc_post_office,
    }

    result = {
        "status_code": status.HTTP_200_OK,
        "message": "Post Office For Registration",
        "data": data,
    }
    return result

@router.post("/submit", response_model=response.APIResponse)
def submit_regisration_data(
    request: RegistrationFormRequestDTO,
    db: Session = Depends(get_db),
    client_ip: str = Depends(get_client_ip),
):
    # print(request)
    noc_application_id = generate_applicantion_id()
    password = hash_password(request.password)
    # print(noc_application_id)

    registration_data = registrationMap(request, noc_application_id, client_ip)
    # print(jsonable_encoder(registration_data))
    login_data = loginMap(password, noc_application_id)
    application_data = form1Map(noc_application_id, client_ip)
    track_data = applicationTrackMap(
        {
            "nocRegId": noc_application_id,
            "remarks": "Registration Done",
            "status": 1,
            "ip": client_ip,
        }
    )

    insert_status = applicantRegistrationService(db).insert_data(
        registration_data, login_data, application_data, track_data
    )
    
    if insert_status:
        data = {"noc_registration_id": noc_application_id}
        result = {
            "status_code": status.HTTP_200_OK,
            "message": "Registration Success",
            "data": data,
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Registration Failed.Please Try Again",
        )
    return result


def generate_applicantion_id():
    now = datetime.now()
    timestamp_part = now.strftime("%Y%m%d%H%M%S")
    noc_application_id = f"NOC{timestamp_part}"

    return noc_application_id
