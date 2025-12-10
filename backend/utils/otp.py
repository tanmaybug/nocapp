from fastapi import status
import random
from redis.asyncio import Redis

OTP_EXPIRE_SECONDS = 600  # 5 minutes
COOLDOWN_SECONDS = 30  # 30 Sec
OTP_RETRY_LIMIT = 5  # max invalid attempts allowed

class OTPService:
    @staticmethod
    async def generate_otp():
        return str(random.randint(100000, 999999))

    @staticmethod
    async def store_otp(r: Redis, phone_mail: str, otp: str):
        key = f"otp:{phone_mail}"
        await r.set(key, otp, ex=OTP_EXPIRE_SECONDS)

        # reset attempt counter
        await r.set(f"otp_attempts:{phone_mail}", 0, ex=OTP_EXPIRE_SECONDS)

    @staticmethod
    async def validate_otp(r: Redis, phone_mail: str, user_otp: str):
        otp_key = f"otp:{phone_mail}"
        attempt_key = f"otp_attempts:{phone_mail}"

        # Fetch stored OTP
        real_otp = await r.get(otp_key)
        if not real_otp:
            return False,status.HTTP_401_UNAUTHORIZED, "OTP expired or not found"

        # Check attempt count
        attempts = int(await r.get(attempt_key) or 0)
        if attempts >= OTP_RETRY_LIMIT:
            return False,status.HTTP_429_TOO_MANY_REQUESTS, "Too many wrong attempts. Try again."

        # If invalid OTP
        if real_otp != user_otp:
            await r.incr(attempt_key)
            return False,status.HTTP_401_UNAUTHORIZED, "Invalid OTP"

        # OTP correct → delete OTP + attempts
        await r.delete(otp_key)
        await r.delete(attempt_key)
        return True,status.HTTP_200_OK, "OTP verified successfully"
    
    @staticmethod
    async def can_send_otp(r: Redis, phone_mail: str):
        key = f"otp_cooldown:{phone_mail}"

        # If key exists → user still in cooldown period
        if await r.exists(key):
            return False

        # Set cooldown key for 30 seconds
        await r.set(key, 1, ex=COOLDOWN_SECONDS)
        return True
