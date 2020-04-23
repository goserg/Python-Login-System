from account.pickle_manager import PickleManager

# from account.sqlite_manager import SQLiteManager
from window import Window

accounts = PickleManager()
# accounts = SQLiteManager()

window = Window(accounts)

window.run()

accounts.close_manager()
