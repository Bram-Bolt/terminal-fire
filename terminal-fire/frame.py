# type ignore for vscode bugs
import numpy as np  # type: ignore
from function_generator import generate_normal_array
import random
from colour_config import ANSI


class Frame:
    def __init__(self, height, width, config):

        self.frame = np.zeros((height, width), dtype=int)
        self.iters = np.zeros((height, width), dtype=int)

        self.mean = 0.5
        self.std_dev = 0.5
        self.scale_factor = 0.7
        self.y_values = generate_normal_array(self.mean, width, self.std_dev)
        self.colour_encoding, self.seq_encoding = config
        self.max_colour = len(self.seq_encoding) - 1

    def update_frame(self):
        self.frame = np.roll(self.frame, shift=-1, axis=0)
        self.frame[-1, :] = self.max_colour

        self.iters = np.roll(self.frame, shift=-1, axis=0)
        self.iters[-1, :] = 0

    def reduce_frame(self):
        for row_idx, row in enumerate(self.frame):
            for idx, c in enumerate(row):
                p = random.randint(1, 100) / 100
                if self.frame[row_idx][idx] == 0:
                    # If the current cell is empty, do nothing
                    pass
                elif p < (1 - self.y_values[idx]) * self.scale_factor:
                    self.frame[row_idx][idx] -= 1

    def get_coloured_char(self, i):
        c_id = int(self.seq_encoding[i])
        colour, c = self.colour_encoding[c_id]
        return f"{colour.value}{c}{ANSI.RESET.value}"

    def __str__(self):
        coloured_row_strs = []
        for row in self.frame:
            coloured_row = [f"{self.get_coloured_char(i)}" for i in row]
            coloured_row_strs.append("".join(coloured_row))
        return "\n".join(coloured_row_strs)
