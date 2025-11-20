import re

def phoneNumberValidation(phone:int) -> bool:
    pattern = r"^[6-9]\d{9}$"
    if re.fullmatch(pattern, str(phone)) and len(str(phone)) == 10:
        return True
    else:
        return False
    
def pinNumberValidation(pin: int) -> bool:
    pattern = r"^\d{6}$"
    if re.fullmatch(pattern, str(pin)) and len(str(pin)) == 6:
        return True
    else:
        return False