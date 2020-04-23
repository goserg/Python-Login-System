import tkinter as tk
import tkinter.font
import fsm
from typing import Any
from account.data_manager import DataManager
from messengers.messenger import Messenger


class SignInFrame(tk.Frame):
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
        self.root = root
        self.font = font

        self.top_frame = tk.Frame(bg="#e8e8e8")
        self.middle_frame = tk.Frame(bg="#e8e8e8")
        self.bottom_frame = tk.Frame(bg="#e8e8e8")

        self.sign_in_label = tk.Label(
            self.top_frame, text="Sign in", bg="#e8e8e8", font=self.font,
        ).grid()

        self.user_name_label = tk.Label(
            self.middle_frame, text="Name", bg="#e8e8e8", font=self.font,
        ).grid(row=0, sticky=tk.E)

        self.user_name_entry = tk.Entry(
            self.middle_frame, width=30, bg="#d2d2d2", font=self.font,
        )
        self.user_name_entry.grid(row=0, column=1, padx=5)

        self.password_label = tk.Label(
            self.middle_frame, text="Password", bg="#e8e8e8", font=self.font,
        ).grid(row=1, sticky=tk.E)

        self.password_entry = tk.Entry(
            self.middle_frame, width=30, bg="#d2d2d2", show="*", font=self.font,
        )
        self.password_entry.grid(row=1, column=1, padx=5)

        self.sign_in_button = tk.Button(
            self.bottom_frame,
            text="Sign in",
            command=self.sing_in_action,
            bd=1,
            bg="#56cae3",
            fg="white",
            font=self.font,
        ).grid(row=0)

        self.create_account = tk.Button(
            self.bottom_frame,
            text="create account",
            command=self._create_account_action,
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
        self.user_name_entry.focus()

    def hide(self) -> None:
        self.top_frame.grid_forget()
        self.middle_frame.grid_forget()
        self.bottom_frame.grid_forget()

    def sing_in_action(self) -> None:
        if not self.user_name_entry.get() or not self.password_entry.get():
            self.root.messenger.warn("Warning", "Fill all the fields")
            return
        if not self.accounts.is_user_exists(
            self.user_name_entry.get()
        ) or not self.accounts.verify_user(
            self.user_name_entry.get(), self.password_entry.get()
        ):
            self.root.messenger.error("ERROR", "User name or password is incorrect")
            return
        self.root.messenger.notify("Success", "Account verified")

    def _create_account_action(self) -> None:
        self.root.set_state(fsm.State.NEW_ACCOUNT)
