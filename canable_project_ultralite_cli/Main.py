import sys
from Cli import CliAdapter
from var import *


if __name__ == '__main__':
    args = sys.argv
    if args.__len__() == 2:
        if args[1] == HELP_S or args[1] == HELP_L:
            print(HELP_TEXT)
        else:
            app = CliAdapter()
    sys.exit(0)
