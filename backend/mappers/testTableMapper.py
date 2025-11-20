from dtos.testFormDTO import TestFormRequestDTO
from models.testTableModel import Post

def dbtodto(data:Post):
    pass

def dtotodb(data: TestFormRequestDTO) -> Post:
    result = Post(
        name=data.name,
        phone=data.phone_number,
        email=data.email,
        create_ip="127.0.0.1",
    )

    return result