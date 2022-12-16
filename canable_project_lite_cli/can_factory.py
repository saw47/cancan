import threading
import time
import can

from Input import Input
from var import ZERO_LEVEL_2, flags_zero_level, STOP, EXIT, user_inp
from util import fill_who_run_now
from bus import lada_ph2_bus


def select_lib(arg: str, adapter: Input):
    pass

def run_command(arg: str, adapter: Input):
    input_adapter = adapter
    if arg in list(ZERO_LEVEL_2.keys()) and arg != STOP:

        if not flags_zero_level.get(arg):
            bus = lada_ph2_bus
            frame = HumaxLib(arg, bus)
            frame.start()
    else:
        print("I am dummy, next level not implemented")

def dead_command():
    pass


# ---------------------------------------------
# List of commands for fast call via cli command
# ---------------------------------------------

# TODO позже прикрутить либы в жсоне и десериализацию, не хардкодить пакеты тут
class HumaxLib(threading.Thread):

    def __init__(self, arg: str, bus: can.Bus):
        super().__init__()
        self.argument: str = arg
        self.input_index: str = user_inp
        self.bus = bus

    def run(self) -> None:
      #TODO закончил тут нужно проработать старт стоп приложения

        command_list = list(ZERO_LEVEL_2.keys())

        while not self.input_index == STOP or self.input_index == EXIT:
            if self.argument == command_list[0]:
                self.wake_up_lvl3(self.bus)
            elif self.argument == command_list[1]:
                self.wake_up_lvl2_conservative(self.bus)
            elif self.argument == command_list[2]:
                self.wake_up_lvl3_with_cluster(self.bus)
            else:
                raise Exception(f"Illegal arguments -->> |{self.argument}|")

    def wake_up_lvl3(self, bus):
        while True:
            message = can.Message(arbitration_id=0x62C,
                                  data=[0x00],
                                  is_extended_id=False)
            print(f"run -> id {message.arbitration_id} -->> message {message.data}")
            bus.send(message)
            fill_who_run_now(str(f"{message.arbitration_id}-->>{message.data}"))
            time.sleep(0.05)

            message = can.Message(arbitration_id=0x666,
                                  data=[0x00, 0x00, 0x00, 0x00],
                                  is_extended_id=False)
            print(f"run -> id {message.arbitration_id} -->> message {message.data}")
            bus.send(message)
            fill_who_run_now(str(f"{message.arbitration_id}-->>{message.data}"))
            time.sleep(0.05)

            message = can.Message(arbitration_id=0x350,
                                  data=[0xC5, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                                  is_extended_id=False)
            print(f"run -> id {message.arbitration_id} -->> message {message.data}")
            bus.send(message)
            fill_who_run_now(str(f"{message.arbitration_id}-->>{message.data}"))
            time.sleep(0.05)

            message = can.Message(arbitration_id=0x55D,
                                  data=[0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                                  is_extended_id=False)
            print(f"run -> id {message.arbitration_id} -->> message {message.data}")
            bus.send(message)
            fill_who_run_now(str(f"{message.arbitration_id}-->>{message.data}"))
            time.sleep(0.05)

    def wake_up_lvl2_conservative(self, bus):
        while True:
            message = can.Message(arbitration_id=0x350,
                                  data=[0xC7, 0x07, 0x18, 0x1F, 0x14, 0xC8, 0x94, 0x85],
                                  is_extended_id=False)
            print(f"run -> id {message.arbitration_id} -->> message {message.data}")
            bus.send(message)
            fill_who_run_now(str(f"{message.arbitration_id}-->>{message.data}"))
            time.sleep(0.1)

            message = can.Message(arbitration_id=0x55D,
                                  data=[0x00, 0xDD, 0x60, 0xC0, 0x92, 0x80, 0x00, 0x00],
                                  is_extended_id=False)
            print(f"run -> id {message.arbitration_id} -->> message {message.data}")
            bus.send(message)
            fill_who_run_now(str(f"{message.arbitration_id}-->>{message.data}"))
            time.sleep(0.1)

    def wake_up_lvl3_with_cluster(self, bus):
        while True:
            message = can.Message(arbitration_id=0x62C,
                                  data=[0x00],
                                  is_extended_id=False)
            print(f"run -> id {message.arbitration_id} -->> message {message.data}")
            bus.send(message)
            fill_who_run_now(str(f"{message.arbitration_id}-->>{message.data}"))
            time.sleep(0.05)

            message = can.Message(arbitration_id=0x666,
                                  data=[0x00, 0x00, 0x00, 0x00],
                                  is_extended_id=False)
            print(f"run -> id {message.arbitration_id} -->> message {message.data}")
            bus.send(message)
            fill_who_run_now(str(f"{message.arbitration_id}-->>{message.data}"))
            time.sleep(0.05)

            message = can.Message(arbitration_id=0x350,
                                  data=[0xC5, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                                  is_extended_id=False)
            print(f"run -> id {message.arbitration_id} -->> message {message.data}")
            bus.send(message)
            fill_who_run_now(str(f"{message.arbitration_id}-->>{message.data}"))
            time.sleep(0.05)

            message = can.Message(arbitration_id=0x55D,
                                  data=[0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                                  is_extended_id=False)
            print(f"run -> id {message.arbitration_id} -->> message {message.data}")
            bus.send(message)
            fill_who_run_now(str(f"{message.arbitration_id}-->>{message.data}"))
            time.sleep(0.05)

            # TODO add two frame from cluster
