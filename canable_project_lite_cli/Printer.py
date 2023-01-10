import var


class Printer:
    def __init__(self):
        print(" -> printer is created")

    def print_local(self):
        print(var.printed_value, end=f"printer is work, interrupt in printer-> {var.input_interrupt} \n")
        var.input_interrupt = False


