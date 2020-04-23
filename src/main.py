import input_manager
import output_manager
import window_manager
# from account.pickle_account_manager import PickleAccountManager
from account.sqlite_account_manager import SQLiteAccountManager
from fsm import State
import logic


# accounts = PickleAccountManager()
accounts = SQLiteAccountManager()

state = State.MENU
action = 0

while True:
    action = 0
    if state == State.MENU:
        try:
            action = input_manager.select_action()
        except ValueError:
            output_manager.display_message("wrong command")
            continue
        if action == 1:
            state = State.NEW_ACCOUNT
        elif action == 2:
            state = State.VERIFICATION
        elif action == 3:
            state = State.PASSWORD_CHANGE
        elif action == 4:
            print(accounts.get_users())
            output_manager.wait()
        else:
            output_manager.notify("wrong command")
    elif state == State.NEW_ACCOUNT:
        window_manager.clear_screen()
        print("NEW ACCOUNT CREATION")
        name = logic.ask_for_user_name()
        logic.add_user(name, accounts)
        state = State.MENU
    elif state == State.VERIFICATION:
        window_manager.clear_screen()
        print("VERIFICATION")
        name = logic.ask_for_user_name()
        logic.verify_user(name, accounts)
        state = State.MENU
    elif state == State.PASSWORD_CHANGE:
        window_manager.clear_screen()
        print("PASSWORD CHANGE")
        name = logic.ask_for_user_name()
        logic.change_password(name, accounts)
        state = State.MENU

accounts.close_manager()
