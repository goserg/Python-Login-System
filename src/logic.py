import input_manager
import output_manager
import tools
import errors
from account.account_manager import AccountManager


def ask_for_user_name() -> str:
    name = input_manager.request_user_name()
    return name


def add_user(name: str, accounts: AccountManager) -> bool:
    try:
        tools.name_validation(name)
    except errors.UserNameError as err:
        print(*err.args)
        output_manager.wait()
        return False
    if accounts.is_user_exists(name):
        output_manager.notify(f"name {name} is taken")
        return False
    password = input_manager.request_password()
    try:
        tools.password_validation(password)
    except errors.PasswordError as err:
        print(*err.args)
        output_manager.wait()
        return False
    conf_password = input_manager.request_confirmation()
    if conf_password != password:
        output_manager.notify("passwords did not match!")
        return False

    accounts.add_user(name, tools.hash_password(password))
    output_manager.notify(f"user {name} successfully added")
    return True


def change_password(name: str, accounts: AccountManager) -> bool:
    if not verify_user(name, accounts):
        return False
    password = input_manager.request_new_password()
    try:
        tools.password_validation(password)
    except errors.PasswordError:
        return False
    new_password = input_manager.request_confirmation()
    if password != new_password:
        output_manager.notify("passwords did not match")
        return False
    accounts.change_password(name, tools.hash_password(password))
    output_manager.notify("password change")
    return True


def verify_user(name: str, accounts: AccountManager) -> bool:
    if not accounts.is_user_exists(name):
        output_manager.notify("User not exists")
        return False
    password = input_manager.request_password()
    if accounts.verify_user(name, password):
        output_manager.notify("User verified")
        return True
    else:
        output_manager.notify("Invalid password")
        return False
