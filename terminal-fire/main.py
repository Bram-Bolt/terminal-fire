from animator import animate_sequence
from colour_config import colour_encoding, seq_encoding
import os


w, h = os.get_terminal_size()

config = (colour_encoding, seq_encoding)
animate_sequence(10, h, w, config)
