import tkinter as tk
import tkinter.font
from account.data_manager import DataManager
from messengers.tkinter_messenger import TkinterMessenger
from frames.sign_in_frame import SignInFrame
from frames.new_account_frame import NewAccountFrame
import fsm


class Window:
    def __init__(self, accounts: DataManager) -> None:
        self.accounts = accounts
        self.state = fsm.State.VERIFICATION

        self.messenger = TkinterMessenger()

        self.root = tk.Tk()
        self.root.title("Login system")
        self.root.configure(background="#e8e8e8")

        self.center_window()
        self.root.resizable(0, 0)

        self.root.bind("<Return>", self.on_enter_press)

        self.font = tkinter.font.Font(family="Helvetica")
        self.sign_in_frame = SignInFrame(self.accounts, self.messenger, self.font, self)
        self.create_frame = NewAccountFrame(
            self.accounts, self.messenger, self.font, self
        )
        self.frames = [self.sign_in_frame, self.create_frame]
        self.set_state(fsm.State.VERIFICATION)

    def set_state(self, state: fsm.State) -> None:
        self.state = state
        for i in self.frames:
            i.hide()
        if self.state == fsm.State.VERIFICATION:
            self.sign_in_frame.show()
        elif self.state == fsm.State.NEW_ACCOUNT:
            self.create_frame.show()

    def center_window(self) -> None:
        self.root.withdraw()
        self.root.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry("+%d+%d" % (x, y))
        self.root.deiconify()

    def run(self) -> None:
        self.root.mainloop()

    def on_enter_press(self, _: tk.Event) -> None:
        if self.state == fsm.State.VERIFICATION:
            self.sign_in_frame.sing_in_action()
        elif self.state == fsm.State.NEW_ACCOUNT:
            self.create_frame.confirm_action()
