# type ignore for vscode bugs
import numpy as np  # type: ignore
from .function_generator import generate_normal_array
from .colour_config import ANSI


# TODO need better name for "age", since it goes down. "lives" sounds a bit weird?
class Frame:
    def __init__(self, height, width, config):
        self.frame = np.zeros((height, width), dtype=int)

        # TODO STEP A WAY FROM HARDCODING!!! SHOULD BE DYNAMIC BASED ON LENGTH
        self.scale_factor = 0.7  # scaling factor for treshold

        self.mean = 0.5
        self.std_dev = 0.5
        self.normal_dist_array = generate_normal_array(self.mean, width, self.std_dev)

        self.colour_encoding, self.seq_encoding = config  # sets encoding
        self.starting_age = len(self.seq_encoding) - 1  # sets starting char age

    def shift_frame(self):
        """Shift the ids in the frame upwards, resetting the new bottom row"""
        self.frame = np.roll(self.frame, shift=-1, axis=0)
        self.frame[-1, :] = self.starting_age

    def age_frame(self):
        """Age alls items in frame based on probabilities and the distribution array."""

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

    def get_coloured_char(self, age):
        """Return the ANSI colored character for the given char age"""
        c_id = int(self.seq_encoding[age])
        colour, c = self.colour_encoding[c_id]
        return f"{colour.value}{c}{ANSI.RESET.value}"

    def __str__(self):
        """Convert the frame to a string with colored characters."""

        # Vectors are similar to maps, but are used on np.arrays.
        # Vectorisation changes the elements from their id to a coloured string representation
        vectorized_coloured_char = np.vectorize(self.get_coloured_char)
        coloured_frame = vectorized_coloured_char(self.frame)

        # Combine coloured characters lists in to string.
        return "\n".join("".join(row) for row in coloured_frame)
