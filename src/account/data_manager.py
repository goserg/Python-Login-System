from abc import ABC


class DataManager(ABC):
    def is_user_exists(self, name: str) -> bool:
        pass

    def verify_user(self, name: str, password: str) -> bool:
        pass

    def add_user(self, name: str, hashed_password: str) -> None:
        pass

    def change_password(self, name: str, hashed_password: str) -> None:
        pass

    def get_users(self) -> tuple:
        pass

    def close_manager(self) -> None:
        pass
