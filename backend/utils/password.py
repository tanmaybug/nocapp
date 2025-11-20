from passlib.context import CryptContext
import random
import string

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_password()->str:
    length = 10

    # Required character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "@#$&"

    # Ensure at least one from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill the remaining characters
    all_chars = uppercase + lowercase + digits + special
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable placement
    random.shuffle(password)

    return "".join(password)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        x = pwd_context.verify(plain_password, hashed_password)
        if x:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
