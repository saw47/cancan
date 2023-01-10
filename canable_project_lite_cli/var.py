# CONST

SECOND: float = 1.00

INVALID_ARGUMENT: str = "Invalid argument"

STOP: str = "d"
EXIT: str = "q"

# var
level: int = 0
user_inp = ""
printed_value = ""
input_interrupt: bool = False

# help and start scripts
HELP_S: str = "-h"
HELP_L: str = "--help"
VERSION: str = "CANable CLI client\nversion B0"
WELCOME: str = "Hi, i'am CanCan mazafacka"
HELP_TEXT: str = f"TODO"

# First level selector -> select car
LADA_GRANTA_ENJOY_PRO: str = "g"
LADA_VESTA_ENJOY_PRO: str = "v"
LADA_VESTA_ENJOY_VISION_PRO: str = "p"
PRINTER_CAR_SELECT: str = f"Select car and can protocol:\n" \
                    f"LADA_VESTA_ENJOY_PRO -> {LADA_VESTA_ENJOY_PRO};\n" \
                    f"LADA_GRANTA_ENJOY_PRO -> {LADA_GRANTA_ENJOY_PRO};\n" \
                    f"LADA_VESTA_ENJOY_VISION_PRO -> {LADA_VESTA_ENJOY_VISION_PRO}.\n"
