from animator import animate_sequence
from colour_config import colour_encoding, seq_encoding

h = 40
w = 100

config = (colour_encoding, seq_encoding)
animate_sequence(10, h, w, config)
