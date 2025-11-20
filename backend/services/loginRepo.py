from sqlalchemy.orm import Session
from models.loginTableModel import Login
from fastapi.encoders import jsonable_encoder


class loginService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self,username):
        result = (
            self.db.query(Login)
            .filter(Login.active_status == 1)
            .filter(Login.stake_user == username)
            .all()
        )

        if len(result) > 0:
            return jsonable_encoder(result)[0]
        else:
            return False
        
    def update_token(self,userId:str,token:str):
        pass
        # Construct the update statement
        # stmt = (
        #     update(Login)
        #     .where(Login.stake_user == userId)
        #     .values(tokenlogin_token=token)
        # )

        # # Execute the update
        # with self.db.connect() as conn:
        #     conn.execute(stmt)
        #     conn.commit() # Commit the transaction
