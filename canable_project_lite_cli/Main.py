import sys
from Cli import Cli
from Adapter import Adapter
import var
from com_port.com_permission import getComPermission


def run(arg=None):
    print(f"{var.VERSION}\n{var.WELCOME}")

    if args.__len__() == 2:
        if args[1] == var.HELP_S or args[1] == var.HELP_L:
            print(var.HELP_TEXT)
    else:
        # if sys.platform == "linux" or sys.platform == "linux2":
        #    getComPermission()
        # TODO ne proebat raskomentit after realise can factory

        app = Cli(arg)
        can_adapter = Adapter()

        while var.user_inp != var.EXIT:
            app.run()
            can_adapter.run()


if __name__ == '__main__':
    args = sys.argv
    if args.__len__() == 2:
        while var.user_inp != var.EXIT:
            run(args[1])
    elif args.__len__() == 1:
        run()
    else:
        print(var.INVALID_ARGUMENT)
    sys.exit(0)
