import serial.tools.list_ports
from sys import platform


# -------------------------------------
#       Functions
# -------------------------------------
def auto_port_scan():  # Find right COM port
    if os_definition() == "win32":
        right_port = port_finding_windows()
    elif os_definition() == "darwin":
        right_port = port_finding_mac_linux()
    elif os_definition() == "linux" or "linux2":
        right_port = port_finding_mac_linux()
    return right_port


def os_definition():  # OS definition
    if platform == "linux" or platform == "linux2":
        # linux ...
        return platform
    elif platform == "darwin":
        # OS X ...
        return platform
    elif platform == "win32":
        # Windows ...
        return platform


def port_finding_windows():  # Find right COM-port for windows
    ports = list(serial.tools.list_ports.comports())
    __port__ = ""
    for p in ports:
        if "CANtact" in p[1]:
            print("Port: {0}".format(p[0]))
            print("Device name: {0}".format(p[1]))
            print("USB Data: {0}".format(p[2]))
            __port__ = p[0]
    if __port__ == "":
        print("COM port not found")
    return __port__


def port_finding_mac_linux():  # Find right COM-port for MAC and Linux
    ports = list(serial.tools.list_ports.comports())
    __port__ = ""
    for p in ports:
        if "CAN" in p[1]:
            print("Port: {0}".format(p[0]))
            print("Device name: {0}".format(p[1]))
            print("USB Data: {0}".format(p[2]))
            __port__ = p[0]
    if __port__ == "":
        print("COM port not found")
    return __port__