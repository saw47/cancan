# var
level: int = 0

user_inp = ""


def get_user_inp() -> str:
    return user_inp


def set_user_inp(inp: str):
    global user_inp
    user_inp = inp


# CONST

HELP_TEXT: str = "Здесь будет хелп"

EXIT: str = "q"
END: str = "d"

CARS_CMD: list = [
    ("v", "Vesta с lvl2 aka Lada Vesta Enjoy Pro"),
    ("n", "Vesta с lvl3 aka Lada Vesta Enjoy Vision Pro"),
    ("g", "Granta с lvl2 aka Lada Granta Enjoy Pro"),
    ("x", "X-Ray с lvl2 aka Lada X-Ray Enjoy Pro"),
    ("q", "Покинуть чат")
]

V_LVL2_CMD: list = [
    ("q", "Покинуть чат"),
    ("d", "остановить то, что сейчас работает"),
    ("l", "посмотреть - что сейчас работает"),
    ("1", "wake up head unit"),
    ("2", "shut down head unit"),
    ("3", "pull the handbrake")
]

V_LVL3_CMD: list = [
    ("q", "Покинуть чат"),
    ("d", "остановить то, что сейчас работает"),
    ("l", "посмотреть - что сейчас работает"),
    ("1", "wake up head unit & cluster"),
    ("2", "shut down head unit"),
    ("3", "pull the handbrake")
]
G_LVL2_CMD: list = [
    ("q", "Покинуть чат"),
    ("d", "остановить то, что сейчас работает"),
    ("l", "посмотреть - что сейчас работает"),
    ("1", "pull the handbrake")
]

LEVEL_TWO: list = [
    (CARS_CMD[0][0], V_LVL2_CMD),
    (CARS_CMD[1][0], V_LVL3_CMD),
    (CARS_CMD[2][0], G_LVL2_CMD)
]

HELP_S: str = "-h"
HELP_L: str = "--help"
DOWN: str = "↓^↓^↓ Ввод в строке ниже ↓^↓^↓"

VERSION: str = "CANable ultralite CLI client <version B1> "

INVALID_ARG: str = "Нет такой команды"
NOT_IMPL: str = "Это не поддерживается, через 1 сек будет выброс"
