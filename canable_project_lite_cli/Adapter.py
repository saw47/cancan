import threading

global user_inp
global printed_value


class Adapter(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        print(" -> adapter is started")
