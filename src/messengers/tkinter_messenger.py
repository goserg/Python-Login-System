import tkinter.messagebox
from messengers.messenger import Messenger


class TkinterMessenger(Messenger):
    def notify(self, message_type: str, text: str) -> None:
        tkinter.messagebox.showinfo(message_type, text)

    def warn(self, message_type: str, text: str) -> None:
        tkinter.messagebox.showwarning(message_type, text)

    def error(self, message_type: str, text: str) -> None:
        tkinter.messagebox.showerror(message_type, text)
