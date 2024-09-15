from enum import Enum


class ANSI(Enum):
    RED = "\033[91m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    CLEAR = "\033[49m"
    WHITE = "\33[0;97m"
    GRAY = "\033[90m"
    RESET = "\033[0m"


colour_encoding = {
    0: (ANSI.CLEAR, " "),
    1: (ANSI.GRAY, "+"),
    2: (ANSI.RED, "x"),
    4: (ANSI.YELLOW, "%"),
    5: (ANSI.WHITE, "@"),
}


seq_encoding = "0110002245"
