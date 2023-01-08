import threading
import time
from Printer import Printer
from InputAdapter import InputAdapter
import var


class Cli(threading.Thread):
    inp_value = var.user_inp

    def __init__(self, arg):
        argument = arg  # TODO prikrutit obrabotku argumenta
        super().__init__()
        print(" -> CLI is created")

    def run(self) -> None:
        printer = Printer()
        inp = InputAdapter()
        print("CLI Run")
        var.printed_value = var.PRINTER_CAR_SELECT
        printer.print_local()

        while var.user_inp != var.EXIT:
            print("while loop in CLI run!!!")
            if not var.input_interrupt:
                inp.run()
                print("inp Run interrupt 222 in CLI False")
            else:
                if self.inp_value != var.user_inp:
                    print(f"self.inp_value != var.user_inp, {self.inp_value} != {var.user_inp}")
                    # var.input_interrupt = True
                    # var.printed_value = f"input -> {var.user_inp}self inp value-{self.inp_value}"
                    printer.print_local()
                    self.inp_value = var.user_inp
                    time.sleep(var.SECOND)
                    var.input_interrupt = False
                    print(f"inp Run interrupt new value from CLI -> {var.input_interrupt}")
                    # inp.run()
                else:
                    print(f"self.inp_value = var.user_inp, {self.inp_value} = {var.user_inp}")
                    print(f"inp Run interrupt ---->>>  {var.input_interrupt}")
                    time.sleep(var.SECOND)







