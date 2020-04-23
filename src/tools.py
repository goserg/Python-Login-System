import errors
import uuid
import hashlib

MIN_PASSWORD_LEN = 8


def password_validation(password: str) -> None:
    """
    Basic password validation check.
    :param password: user password
    """
    if not password.strip():
        raise errors.PasswordError("ERROR: empty password")
    if len(password) < MIN_PASSWORD_LEN:
        raise errors.PasswordError(
            f"ERROR: password mast be at least {MIN_PASSWORD_LEN} character long"
        )
    return None


def name_validation(name: str) -> None:
    """
    Basic name validation check. Raises errors.UserNameError
    :param name: user password
    """
    if not name.strip():
        raise errors.UserNameError("ERROR: empty name")
    if name[0] == " " or name[-1] == " ":
        raise errors.UserNameError("ERROR: name can not starts or ends with space")
    return None


def hash_password(password: str) -> str:
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt


def check_password(hashed: str, user_password: str) -> bool:
    password, salt = hashed.split(":")
    return (
        password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
    )
