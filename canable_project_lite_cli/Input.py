import threading

global user_inp


class Input(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self) -> None:
        global user_inp

        while True:
            inp = Input()
            user_inp = str(inp)
