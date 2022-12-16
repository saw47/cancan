import threading
import time
import can
from can import Bus
from var import *
from util import list_printer
from connection_mode import auto_port_scan

humax_bus = Bus(
    bustype='slcan',
    channel=auto_port_scan(),
    bitrate=500000)

run_now: set = set()


def car_command(arg: str):
    for i in LEVEL_TWO:
        if i == arg:
            list_printer(i[1])
    inp_th = threading.Thread(target=inp, daemon=True)
    out_th = threading.Thread(target=can_run, args=(arg,))
    inp_th.start()
    out_th.start()


def inp():
    while get_user_inp() != EXIT:
        inp = str(input())
        set_user_inp(inp)


def can_run(car_arg: str):
    inp_arg = get_user_inp()
    car = car_arg
    if car_arg == CARS_CMD[0][0]:
        car = VestaLevelTwo(humax_bus)
    elif car_arg == CARS_CMD[1][0]:
        car = VestaLevelThree(humax_bus)
    elif car_arg == CARS_CMD[3][0]:
        car = GrantaLevelTwo(humax_bus)
    elif car_arg == CARS_CMD[4][0]:
        car = XRayLevelTwo(humax_bus)


# ---------------------------------------------
# List of commands for fast call via cli command
# ---------------------------------------------

class GrantaLevelTwo:
    bus: can.Bus

    def __init__(self, bus):
        self.bus = bus
        while get_user_inp() != EXIT:
            while get_user_inp() != END:
                if get_user_inp() == G_LVL2_CMD[0][0]:
                    print(G_LVL2_CMD[0][1])
                elif get_user_inp() == G_LVL2_CMD[1][0]:
                    print(G_LVL2_CMD[1][1])
                    run_now.clear()
                elif get_user_inp() == G_LVL2_CMD[2][0]:
                    print(G_LVL2_CMD[2][1])
                    for i in run_now:
                        print(i)
                elif get_user_inp() == G_LVL2_CMD[3][0]:
                    print(G_LVL2_CMD[3][1])
                    self.hand_brake(bus)

    def hand_brake(self, bus):
        delay = 1
        message = can.Message(arbitration_id=0x2DE,
                              data=[0x00, 0x00, 0x01, 0x08, 0x00, 0x00, 0xB0, 0x00],
                              is_extended_id=False)
        log_frame_add(message.arbitration_id, message.data, delay)
        bus.send(message)
        time.sleep(delay)


class XRayLevelTwo:
    bus: can.Bus

    def __init__(self, bus):
        self.bus = bus
        while get_user_inp() != EXIT:
            while get_user_inp() != END:
                if get_user_inp() == G_LVL2_CMD[0][0]:
                    print(G_LVL2_CMD[0][1])
                elif get_user_inp() == G_LVL2_CMD[1][0]:
                    print(G_LVL2_CMD[1][1])
                    run_now.clear()
                elif get_user_inp() == G_LVL2_CMD[2][0]:
                    print(G_LVL2_CMD[2][1])
                    for i in run_now:
                        print(i)
                elif get_user_inp() == G_LVL2_CMD[3][0]:
                    print(G_LVL2_CMD[3][1])
                    self.hand_brake(bus)


class VestaLevelThree:
    bus: can.Bus

    def __init__(self, bus):
        self.bus = bus
        while get_user_inp() != EXIT:
            while get_user_inp() != END:
                if get_user_inp() == G_LVL2_CMD[0][0]:
                    print(G_LVL2_CMD[0][1])
                elif get_user_inp() == G_LVL2_CMD[1][0]:
                    print(G_LVL2_CMD[1][1])
                    run_now.clear()
                elif get_user_inp() == G_LVL2_CMD[2][0]:
                    print(G_LVL2_CMD[2][1])
                    for i in run_now:
                        print(i)
                elif get_user_inp() == G_LVL2_CMD[3][0]:
                    print(G_LVL2_CMD[3][1])
                    self.hand_brake(bus)


class VestaLevelTwo:
    bus: can.Bus

    def __init__(self, bus):
        self.bus = bus
        while get_user_inp() != EXIT:
            while get_user_inp() != END:
                if get_user_inp() == G_LVL2_CMD[0][0]:
                    print(G_LVL2_CMD[0][1])
                elif get_user_inp() == G_LVL2_CMD[1][0]:
                    print(G_LVL2_CMD[1][1])
                    run_now.clear()
                elif get_user_inp() == G_LVL2_CMD[2][0]:
                    print(G_LVL2_CMD[2][1])
                    for i in run_now:
                        print(i)
                elif get_user_inp() == G_LVL2_CMD[3][0]:
                    print(G_LVL2_CMD[3][1])
                    self.hand_brake(bus)


def log_frame_add(id: int, data: bytearray, delay: float):
    key = hex(id)
    values: list = []
    for item in data:
        values.append(hex(item))
    run_now.add(f"{key} {values} delay {delay}")


"""@staticmethod
def wake_up_lvl3_with_cluster(bus):
    while True:
        global counter

        message = can.Message(arbitration_id=0x62C,
                              data=[0x00],
                              is_extended_id=False)
        log_frame(message.arbitration_id, message.data)
        bus.send(message)
        counter = counter + 1
        time.sleep(0.05)

        message = can.Message(arbitration_id=0x666,
                              data=[0x00, 0x00, 0x00, 0x00],
                              is_extended_id=False)
        log_frame(message.arbitration_id, message.data)
        bus.send(message)
        counter = counter + 1
        time.sleep(0.05)

        message = can.Message(arbitration_id=0x350,
                              data=[0xC5, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                              is_extended_id=False)
        log_frame(message.arbitration_id, message.data)
        bus.send(message)
        counter = counter + 1
        time.sleep(0.05)

        message = can.Message(arbitration_id=0x55D,
                              data=[0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                              is_extended_id=False)
        log_frame(message.arbitration_id, message.data)
        bus.send(message)
        counter = counter + 1
        time.sleep(0.05)

        message = can.Message(arbitration_id=0x4F8,
                              data=[0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                              is_extended_id=False)
        log_frame(message.arbitration_id, message.data)
        bus.send(message)
        counter = counter + 1
        time.sleep(0.05)

        message = can.Message(arbitration_id=0x653,
                              data=[0x00, 0x00, 0x00, 0x00],
                              is_extended_id=False)
        log_frame(message.arbitration_id, message.data)
        bus.send(message)
        counter = counter + 1
        time.sleep(0.05)

        message = can.Message(arbitration_id=0x699,
                              data=[0x00, 0x2C, 0x04, 0x30, 0x00, 0x00, 0x00, 0x00],
                              is_extended_id=False)
        log_frame(message.arbitration_id, message.data)
        bus.send(message)
        counter = counter + 1
        time.sleep(0.05)"""
