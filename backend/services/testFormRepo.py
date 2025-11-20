from sqlalchemy.orm import Session
from models.testTableModel import Post


class testService:
    def __init__(self, db: Session):
        self.db=db

    def adddata(self, data: Post) -> bool:
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return True

    # def insertData(data:Post,db: Session = Depends(get_db)):
    #     db.add(data)
    #     db.commit()
    #     db.refresh(data)
    #     return True
