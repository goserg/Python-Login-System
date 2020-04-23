def display_message(msg: str) -> None:
    print(msg)


def wait() -> None:
    print("press enter")
    input()


def notify(msg: str) -> None:
    display_message(msg)
    wait()
