from account.account_manager import AccountManager
import output_manager
import window_manager
import tools
import pickle
import os


class PickleAccountManager(AccountManager):
    def __init__(self) -> None:
        self._save_dir = "../data/"
        self._file_name = "".join((self._save_dir + "accounts.acc"))
        self.accounts_data = {}
        if not os.path.isfile(self._file_name):
            if not os.path.exists(self._save_dir):
                os.makedirs(self._save_dir)
        else:
            with open(self._file_name, "rb") as fr:
                try:
                    self.accounts_data = pickle.load(fr)
                except EOFError:
                    window_manager.clear_screen()
                    print("".join(["ERROR: ", self._file_name, " file is corrupted. Try to delete the file"]))
                    output_manager.wait()
                    window_manager.close_app()

    def is_user_exists(self, name: str) -> bool:
        if name in self.accounts_data.keys():
            return True

    def verify_user(self, name: str, password: str) -> bool:
        if tools.check_password(self.accounts_data[name], password):
            return True

    def add_user(self, name: str, hashed_password: str) -> None:
        self.accounts_data[name] = hashed_password
        self._save_accounts()

    def change_password(self, name: str, hashed_password: str) -> None:
        self.accounts_data[name] = hashed_password
        self._save_accounts()

    def get_users(self) -> tuple:
        return tuple(self.accounts_data.keys())

    def _save_accounts(self) -> None:
        with open(self._file_name, "wb") as fw:
            pickle.dump(self.accounts_data, fw)
