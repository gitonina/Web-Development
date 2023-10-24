import re
import filetype

def validate_username(value):
    re2= r'^[a-zA-Z ]+$'
    a= bool(re.match(re2,value))
    return value and len(value) >=3 and len(value)<=80 and a


def validate_email(email):
    if not email:
        return False

    # Longitud máxima de 30 caracteres
    length_valid = len(email) <= 30

    # Expresión regular para validar el formato
    pattern = r'^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
    format_valid = bool(re.match(pattern, email))

    return length_valid and format_valid


def validate_phone_number(phone_number):
    if not phone_number:
        return False

    # Longitud máxima de 15 caracteres
    length_valid = len(phone_number) <= 15

    # Expresión regular para validar el formato
    pattern = r'^(\+569|(\+562))\s\d{4}\d{4}$'
    format_valid = bool(re.match(pattern, phone_number))

    return length_valid and format_valid




def validate_register_user(username,email,phone):
    return validate_username(username)  and validate_email(email) and validate_phone_number(phone)


def validate_img(conf_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if conf_img is None:
        return False

    # check if the browser submitted an empty file
    if conf_img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(conf_img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True


def validate_files(conf_img):
    return  validate_img(conf_img)
