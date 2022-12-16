from util import print_iterator

# var
level: int = 0

user_inp = ""

who_is_run: list = []
work_process: list = []

flags_zero_level: dict = {
    "a": False,
    "s": False,
    "x": False,
    "h": False
}

# CONST

INVALID_ARGUMENT: str = "Невалидный аргумент"

WAIT_INP: str = "Ожидание ввода"

STOP: str = "d"
EXIT: str = "q"

ZERO_LEVEL_2: dict = {
    "a": "разбудить LVL3",
    "s": "разбудить LVL2, который не будится пакетами для LVL3",
    "x": "Разбудить lvl3 c кластером",
    "h": "Что-то более сложное или уникальное",
    "q": "выйти"
}

ZERO_LEVEL: list = [
    ("a", "разбудить LVL3"),
    ("s", "разбудить LVL2, который не будится пакетами для LVL3"),
    ("x", "Разбудить lvl3 c кластером"),
    ("h", "Что-то более сложное или уникальное"),
    ("q", "выйти")
]

HELP_S: str = "-h"
HELP_L: str = "--help"
DOWN: str = "↓^↓^↓ Ввод в строке ниже ↓^↓^↓"

VERSION: str = "CANable lite CLI client\nversion B0"

WELCOME: str = "Привет, я консольный клиент для canable."

HELP_TEXT: str = f"{VERSION}\nКоманды можно передавать в качестве аргументов при запуске или внутри " \
                 f"интерфейса, если есть приглашение к вводу. В CLI команды вводятся в формате " \
                 f"-[команда], в интерфейсе - просто [команда]\nСписок " \
                 f"команд:\n{print_iterator(ZERO_LEVEL)}"
