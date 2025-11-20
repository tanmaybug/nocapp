from dtos.studentDTO import StudentResponseDTO
# from models.studentTableModel import StudentDetails

def dbtodto(data):

    if not data:
        item = None
    else:
        item = StudentResponseDTO(
            student_registration_no=data.student_registration_no,
            student_name=data.student_name,
            phone=data.student_phone_number,
            email=data.student_email_id,
            address=data.student_address,
        )

    return item


def dbtodtolist(data):
    
    if not data:
        y=None
    else:
        y = []
        for x in data:
            y.append(StudentResponseDTO(**x))

    return y
