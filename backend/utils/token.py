import jwt
import datetime

# Secret key for encoding and decoding
SECRET_KEY = "8d9fe9ebb6663c265d68daded700c3c80e46437d"

def create_token(stake_user: str, user_id:int):
    payload = {
        "user_id": user_id,
        "stake_user": stake_user,
        "exp": datetime.datetime.now()
        + datetime.timedelta(minutes=30),  # Token expires in 30 mins
    }
    encode = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    token = encode[::-1]
    return token

def validate_token(token_str:str):
    try:
        token = token_str[::-1]
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print(decoded)
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
    
def decode_token(token_str: str):
    token = token_str[::-1]
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"]) 
