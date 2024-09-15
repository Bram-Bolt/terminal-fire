from animator import animate_sequence
from colour_config import colour_encoding, seq_encoding
import os


config = (colour_encoding, seq_encoding)
animate_sequence(60, config=config, fps=10)
