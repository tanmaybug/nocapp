# from pathlib import Path
# import shutil
# import uuid
# from utils.customFileValidation import validate



# UPLOAD_DIR = Path("../uploads")
# UPLOAD_DIR.mkdir(exist_ok=True)

# if validate(bonafide_certificate):

#     file_ext = Path(bonafide_certificate.filename).suffix
#     bonafide_unique_filename = f"{uuid.uuid4()}{file_ext}"
#     file_path = UPLOAD_DIR / bonafide_unique_filename

#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(bonafide_certificate.file, buffer)
# else:
#     bonafide_unique_filename = None


# if validate(registration_certificate):
#     file_ext = Path(registration_certificate.filename).suffix
#     registration_unique_filename = f"{uuid.uuid4()}{file_ext}"
#     file_path = UPLOAD_DIR / registration_unique_filename

#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(registration_certificate.file, buffer)
# else:
#     registration_unique_filename = None

# file_data = {
#     "bonafide_certificate": 'bonafide_unique_filename',
#     "registration_certificate": 'registration_unique_filename',
# }
