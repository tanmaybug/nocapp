from pydantic import BaseModel

class OTPGetRequest(BaseModel):
    userInput: str

class OTPValidationRequest(BaseModel):
    userInput: str
    otp: str