# type ignore for vscode bugs
import numpy as np  # type: ignore
from function_generator import generate_normal_array
import random
from colour_config import ANSI


class Frame:
    def __init__(self, height, width, config):
        self.frame = np.zeros((height, width), dtype=int)
        self.iters = np.zeros((height, width), dtype=int)

        # STEP A WAY FROM HARDCODING!!! SHOULD BE DYNAMIC BASED ON LENGTH
        self.mean = 0.5
        self.std_dev = 0.5
        self.scale_factor = 0.7

        self.normal_dist_array = generate_normal_array(self.mean, width, self.std_dev)
        self.colour_encoding, self.seq_encoding = config
        self.max_colour = len(self.seq_encoding) - 1

    def shift_frame(self):
        self.frame = np.roll(self.frame, shift=-1, axis=0)
        self.frame[-1, :] = self.max_colour

        self.iters = np.roll(self.frame, shift=-1, axis=0)
        self.iters[-1, :] = 0

    def age_frame(self):
        # Generate random probabilities
        random_probs = np.random.rand(*self.frame.shape)

        # Compute the thresholds
        frame_thresholds = (1 - self.normal_dist_array) * self.scale_factor

        # Check which values should be aged
        aged_mask = random_probs < frame_thresholds

        # Create a mask for non-zero values in the frame
        non_zero_mask = self.frame != 0

        # Apply -1 age on items where both masks hold
        self.frame = np.where(non_zero_mask & aged_mask, self.frame - 1, self.frame)

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
