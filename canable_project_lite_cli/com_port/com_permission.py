import os
import subprocess
import time


def getComPermission():
    print("===Запрос доступа к COM порту===")
    time.sleep(1)
    os.system("sudo -S chmod a+rw /dev/ttyACM0")
    while subprocess.getoutput(
            "chmod a+rw /dev/ttyACM0") == "chmod: cannot access '/dev/ttyACM0': No such file or directory":
        print("!!!Подключите can устройство к порту!!!")
        time.sleep(1)
        os.system("sudo -S chmod a+rw /dev/ttyACM0")
    print("===Доступ получен===")
    return subprocess.getoutput("chmod a+rw /dev/ttyACM0")
