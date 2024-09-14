import numpy as np
import os
import time
import matplotlib.pyplot as plt
import random

h = 40
w = 100

RED = "\033[91m"
BLUE = "\033[94m"
ORANGE = "\033[38;5;214m"  # ANSI escape code for orange (approximated)
YELLOW = "\033[93m"
CLEAR = "\033[49m"
RESET = "\033[0m"

colours = {0: CLEAR, 1: RED, 2: ORANGE, 3: YELLOW}
characters = {0: " ", 1: "x", 2: "o", 3: "@"}


# Parameters
mean = 0.5
length = w  # Example length of the array
std_dev = 0.5  # Example standard deviation
scale_factor = 0.3
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

print(y_values)


class Frame:
    def __init__(self, height, width):
        self.frame = np.zeros((height, width), dtype=int)

    def update_frame(self):
        self.frame = np.roll(self.frame, shift=-1, axis=0)
        self.frame[-1, :] = 3

    def reduce_frame(self):
        for row_idx, row in enumerate(self.frame):
            for idx, c in enumerate(row):
                p = random.randint(1, 100) / 100
                if self.frame[row_idx][idx] == 0:
                    pass
                elif p < (1 - y_values[idx]) * scale_factor:
                    self.frame[row_idx][idx] -= 1

    def __str__(self):
        coloured_row_strs = []
        for row in self.frame:
            coloured_row = [f"{colours[c]}{characters[c]}{RESET}" for c in row]
            coloured_row_strs.append("".join(coloured_row))
        return "\n".join(coloured_row_strs)


canvas = Frame(h, w)

canvas.frame[-1, :] = 1
canvas.frame[10, 10] = 2

for i in range(500):
    print(canvas)
    canvas.update_frame()
    canvas.reduce_frame()
    time.sleep(0.1)
    os.system("clear")
