from sqlalchemy.orm import Session
from models.studentTableModel import StudentDetails


class studentService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self):
        return self.db.query(StudentDetails).filter(StudentDetails.active_status == 1).all()

    def insert_data(self, data: StudentDetails) -> bool:
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return True
