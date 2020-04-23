from console import output_manager, window_manager


def select_action() -> int:
    window_manager.clear_screen()
    output_manager.display_message("Available commands:")
    output_manager.display_message("1: Create new account")
    output_manager.display_message("2: Log in")
    output_manager.display_message("3: Change password")
    output_manager.display_message("4: (show users: test functionality!)")
    try:
        action = int(input())
    except ValueError:
        raise
    else:
        return action


def request_user_name() -> str:
    output_manager.display_message("enter user name")
    return input()


def request_password() -> str:
    output_manager.display_message("enter password")
    return input()


def request_new_password() -> str:
    output_manager.display_message("enter new password")
    return input()


def request_confirmation() -> str:
    output_manager.display_message("confirm password")
    return input()
