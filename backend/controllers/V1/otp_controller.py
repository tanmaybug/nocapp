from fastapi import APIRouter, status
from helpers import response
from config.redis_client import redis
from utils.otp import OTPService
import re

router = APIRouter(prefix="/otp", tags=["MailSMS"])

@router.post("/getOTP")
async def get_otp(userInput: str):

    # check cooldown first
    can_send = await OTPService.can_send_otp(redis, userInput)
    if not can_send:
        result = response.APIResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            message="Please wait 30 seconds before requesting another OTP",
        )
        return result

    otp = await OTPService.generate_otp()
    await OTPService.store_otp(redis, userInput, otp)

    # send OTP via SMS/Mail
    print("Generated OTP:", otp)
    if is_email(userInput):
        print("valid mail")
        result = response.APIResponse(
            status_code=status.HTTP_200_OK, message="OTP sent successfully"
        )
    elif is_phone_number(userInput):
        print("valid phone number")
        result = response.APIResponse(
            status_code=status.HTTP_200_OK, message="OTP sent successfully"
        )
    else:
        print("Invalid Details")
        result = response.APIResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, message="Please Enter Valid Mail Or Phone Number"
        )

    return result

@router.get("/otpVerification")
async def otpVerification(userInput: str,otp:str):
    status, status_code,msg = await OTPService.validate_otp(redis, userInput, otp)
    # data = {"status":status,"message":msg}
    print(f"status:{status} | code:{status_code} | message:{msg}")
    result = response.APIResponse(status_code=status_code, message=msg)
    return result

def is_email(value: str) -> bool:
    # Simple email regex pattern (you may need to refine it based on your specific needs)
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, value) is not None

def is_phone_number(value: str) -> bool:
    # Simple phone number regex pattern (allowing optional country code and common separators)
    phone_pattern = (
        r"^(\+?\d{1,3})?[\s\(\)-]*\d{1,4}[\s\(\)-]*\d{1,4}[\s\(\)-]*\d{1,4}$"
    )
    return re.match(phone_pattern, value) is not None