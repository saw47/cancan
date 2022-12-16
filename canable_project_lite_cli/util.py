import can

from var import who_is_run
from var import user_inp


def print_iterator(item: list):
    for i in item:
        print(f"{i[0]} -> {i[1]}")


def fill_who_run_now(frame: str):
    for item in who_is_run:
        if not frame.__eq__(item):
            who_is_run.append(frame)


def set_user_input(value: str):
    global user_inp
    user_inp = value
