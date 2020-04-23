from abc import ABC


class Messenger(ABC):
    def notify(self, message_type: str, text: str) -> None:
        pass

    def warn(self, message_type: str, text: str) -> None:
        pass

    def error(self, message_type: str, text: str) -> None:
        pass
