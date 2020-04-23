from account.account_manager import AccountManager
import tools
import sqlite3
import os


class SQLiteAccountManager(AccountManager):
    def __init__(self) -> None:
        self._save_dir = "../data/"
        self._file_name = "".join((self._save_dir + "accounts.sdb"))
        if not os.path.exists(self._save_dir):
            os.makedirs(self._save_dir)
        self.sqlite_connection = sqlite3.connect(self._file_name)
        self.cursor = self.sqlite_connection.cursor()

        self._create_table_if_not_exist()

    def close_manager(self) -> None:
        self.sqlite_connection.close()

    def _create_table_if_not_exist(self) -> None:
        try:
            self.cursor.execute("""CREATE TABLE accounts (
                            name text,
                            password text
                            )""")
        except sqlite3.OperationalError:
            pass

    def add_user(self, name: str, hashed_password: str) -> None:
        self.cursor.execute(f"INSERT INTO accounts VALUES ('{name}', '{hashed_password}')")
        self.sqlite_connection.commit()

    def change_password(self, name: str, hashed_password: str) -> None:
        self.cursor.execute(f"UPDATE accounts SET password = '{hashed_password}' WHERE name = '{name}'")
        self.sqlite_connection.commit()

    def is_user_exists(self, name: str) -> bool:
        names = self.get_users()
        if name in names:
            return True

    def verify_user(self, name: str, password: str) -> bool:
        hashed = self.cursor.execute(f"SELECT password FROM accounts WHERE name='{name}'").fetchone()[0]
        if tools.check_password(hashed, password):
            return True

    def get_users(self) -> tuple:
        return tuple(*self.cursor.execute("SELECT name FROM accounts"))

