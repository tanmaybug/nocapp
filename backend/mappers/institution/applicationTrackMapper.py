from dtos.institution.applicationTrackDTO import ApplicationTrackResponse


def application_track_response_dto(db_data):
    response = []
    for index,row in db_data:

        response.append(
            ApplicationTrackResponse(
                sno=index + 1,
                activity=row["status"],
                date=row["insert_date"],
                remarks=row["remarks"],
            )
        )
    return response
