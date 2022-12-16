import sys
from Cli import Cli
from var import VERSION, WELCOME, HELP_L, HELP_S, HELP_TEXT, user_inp, EXIT, INVALID_ARGUMENT
from com_port.com_permission import getComPermission


def run(arg=None):
    print(f"{VERSION}\n{WELCOME}")

    if args[1] == HELP_S or args[1] == HELP_L:
        print(HELP_TEXT)
    else:
        if sys.platform == "linux" or sys.platform == "linux2":
            getComPermission()
        app = Cli(arg)
        while user_inp != EXIT:
            app.start()


if __name__ == '__main__':
    args = sys.argv
    if args.__len__() == 2:
        run(args[1])
    elif args.__len__() == 1:
        run()
    else:
        print(INVALID_ARGUMENT)
    sys.exit(0)
