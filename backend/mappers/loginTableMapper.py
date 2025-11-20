from models.loginTableModel import Login


def dtotodb(password:str, regId:str) -> Login:
    result = Login(stake_user=regId, stake_password=password, active_status=1)
    return result
