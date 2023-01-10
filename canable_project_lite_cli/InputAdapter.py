import threading
import time
import var


class InputAdapter(threading.Thread):

    def __init__(self):
        super().__init__()
        print(" -> INPut adapter is created")

    def run(self) -> None:
        while not var.input_interrupt:
            print(f"input -->>-> interrupt in Input 1 - {var.input_interrupt}")
            inp = input()
            time.sleep(var.SECOND)
            print("!= None!!!!!")
            var.user_inp = str(inp)
            var.printed_value = f"new value - {var.input_interrupt}"
            print(f"input -->>-> 2{var.user_inp}2")
            var.input_interrupt = True
            print(f"input -->>-> interrupt in input adapter new value - {var.input_interrupt}")
            # self.run()
