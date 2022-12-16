import threading
import Adapter
import Watcher
from var import user_inp, EXIT


class Cli(threading.Thread):

    def __init__(self, arg):
        super().__init__()

    def run(self) -> None:
        adapter = Adapter
        watcher = Watcher

