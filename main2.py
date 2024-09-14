import numpy as np
import os
import time
import matplotlib.pyplot as plt
import random

h = 40
w = 100

RED = "\033[91m"
BLUE = "\033[94m"
# ORANGE = "\033[31m"  # ANSI escape code for orange (approximated)
YELLOW = "\033[93m"
CLEAR = "\033[49m"
WHITE = "\33[0;97m"
GRAY = "\033[90m"  # ANSI escape code for gray
RESET = "\033[0m"


colours = {0: CLEAR, 1: GRAY, 2: RED, 4: YELLOW, 5: WHITE}
characters = {0: " ", 1: "+", 2: "x", 3: "o", 4: "%", 5: "@"}


encoding = "0110002245"
print(encoding)


def get_coloured_char(i):
    c = int(encoding[i])
    return f"{colours[c]}{characters[c]}"


# Parameters
max_colour = len(encoding) - 1
mean = 0.5
length = w  # Example length of the array
std_dev = 0.5  # Example standard deviation
scale_factor = 0.7
# Generate the array

import numpy as np
import matplotlib.pyplot as plt


def generate_normal_array(mean, length, std_dev):
    # Generate an array of x-values centered around `mean`
    x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, length)

    # Calculate the PDF values for these x-values
    y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(
        -0.5 * ((x - mean) / std_dev) ** 2
    )

    return x, y


x_values, y_values = generate_normal_array(mean, length, std_dev)


class Frame:
    def __init__(self, height, width):
        self.frame = np.zeros((height, width), dtype=int)
        self.iters = np.zeros((height, width), dtype=int)

    def update_frame(self):
        self.frame = np.roll(self.frame, shift=-1, axis=0)
        self.frame[-1, :] = max_colour

        self.iters = np.roll(self.frame, shift=-1, axis=0)
        self.iters[-1, :] = 0

    def reduce_frame(self):
        for row_idx, row in enumerate(self.frame):
            for idx, c in enumerate(row):
                p = random.randint(1, 100) / 100
                if self.frame[row_idx][idx] == 0:
                    # If the current cell is empty, do nothing
                    pass
                elif p < (1 - y_values[idx]) * scale_factor:
                    self.frame[row_idx][idx] -= 1

    def __str__(self):
        coloured_row_strs = []
        for row in self.frame:
            coloured_row = [f"{get_coloured_char(i)}{RESET}" for i in row]
            coloured_row_strs.append("".join(coloured_row))
        return "\n".join(coloured_row_strs)


canvas = Frame(h, w)


for i in range(500):
    print(canvas)
    canvas.update_frame()
    canvas.reduce_frame()
    time.sleep(0.1)
    os.system("clear")
