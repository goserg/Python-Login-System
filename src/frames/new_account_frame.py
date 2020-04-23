import tkinter as tk
import tkinter.font
import tools
import fsm
from typing import Any
from account.data_manager import DataManager
from messengers.messenger import Messenger


class NewAccountFrame(tk.Frame):
    def __init__(
        self,
        accounts: DataManager,
        messenger: Messenger,
        font: tkinter.font.Font,
        root: Any,
    ) -> None:
        super().__init__()
        self.accounts = accounts
        self.messenger = messenger
        self.font = font
        self.root = root

        self.top_frame = tk.Frame(bg="#e8e8e8")
        self.middle_frame = tk.Frame(bg="#e8e8e8")
        self.bottom_frame = tk.Frame(bg="#e8e8e8")

        self.create_label = tk.Label(
            self.top_frame, text="Create account", bg="#e8e8e8", font=self.font,
        ).grid()

        self.user_name_label = tk.Label(
            self.middle_frame, text="Name", bg="#e8e8e8", font=self.font,
        ).grid(row=0, sticky=tk.E)

        self.user_name_entry = tk.Entry(
            self.middle_frame, width=30, bg="#d2d2d2", font=self.font,
        )
        self.user_name_entry.grid(row=0, column=1)

        self.password_label = tk.Label(
            self.middle_frame, text="Password", bg="#e8e8e8", font=self.font,
        ).grid(row=1, sticky=tk.E)

        self.password_entry = tk.Entry(
            self.middle_frame, width=30, bg="#d2d2d2", show="*", font=self.font,
        )
        self.password_entry.grid(row=1, column=1, padx=5)

        self.confirm_password_label = tk.Label(
            self.middle_frame, text="Confirm", bg="#e8e8e8", font=self.font,
        ).grid(row=2, sticky=tk.E)

        self.confirm_password_entry = tk.Entry(
            self.middle_frame, width=30, bg="#d2d2d2", show="*", font=self.font,
        )
        self.confirm_password_entry.grid(row=2, column=1, padx=5)

        self.confirm_button = tk.Button(
            self.bottom_frame,
            text="Confirm",
            command=self.confirm_action,
            bd=1,
            bg="#56cae3",
            fg="white",
            font=self.font,
        ).grid(row=0)

        self.back_label = tk.Button(
            self.bottom_frame,
            text="back",
            command=self._back_action,
            bd=0,
            bg="#e8e8e8",
            font=self.font,
        ).grid(row=1)

    def show(self) -> None:
        self.top_frame.grid(row=0)
        self.middle_frame.grid(row=1)
        self.bottom_frame.grid(row=2)
        self.user_name_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_password_entry.delete(0, tk.END)
        self.user_name_entry.focus()

    def hide(self) -> None:
        self.top_frame.grid_forget()
        self.middle_frame.grid_forget()
        self.bottom_frame.grid_forget()

    def confirm_action(self) -> None:
        if (
            self._is_name_exist()
            or not self._is_name_valid()
            or not self._is_password_valid()
        ):
            return

        self.accounts.add_user(
            self.user_name_entry.get(), tools.hash_password(self.password_entry.get())
        )
        self.root.messenger.notify("Success", "Account created")
        self.root.set_state(fsm.State.VERIFICATION)

    def _back_action(self) -> None:
        self.root.set_state(fsm.State.VERIFICATION)

    def _is_name_exist(self) -> bool:
        if self.accounts.is_user_exists(self.user_name_entry.get()):
            self.root.messenger.warn("Name error", "User already exists")
            return True

    def _is_name_valid(self) -> bool:
        try:
            tools.name_validation(self.user_name_entry.get())
        except ValueError as err:
            self.root.messenger.warn("Name error", err)
            return False
        return True

    def _is_password_valid(self) -> bool:
        try:
            tools.password_validation(self.password_entry.get())
        except ValueError as err:
            self.root.messenger.warn("Password error", err)
            return False
        return True
