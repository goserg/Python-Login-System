from enum import Enum, auto


class State(Enum):
    MENU = auto()
    NEW_ACCOUNT = auto()
    VERIFICATION = auto()
    PASSWORD_CHANGE = auto()
