import sys
from var import *
from commands import car_command
from com_permission import getComPermission
from util import list_printer


class CliAdapter:
    print(f"{VERSION}")

    def __init__(self, arg):
        super().__init__()
        dialog_run()


def dialog_run():
    list_printer(CARS_CMD)
    inp = input()
    if inp == CARS_CMD[0][0]:
        print(CARS_CMD[0][1])
        car_command(CARS_CMD[0][0])
    elif inp == CARS_CMD[1][0]:
        print(CARS_CMD[1][1])
        car_command(CARS_CMD[1][0])
    elif inp == CARS_CMD[2][0]:
        print(CARS_CMD[2][1])
        car_command(CARS_CMD[2][0])
    elif inp == CARS_CMD[3][0]:
        print(CARS_CMD[3][1])
        car_command(CARS_CMD[3][0])
    elif inp == CARS_CMD[4][0]:
        print(CARS_CMD[4][1])
    else:
        print(INVALID_ARG)
        dialog_run()




