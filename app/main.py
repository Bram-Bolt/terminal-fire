from .animator import animate_sequence
from .colour_config import colour_encoding, seq_encoding
from .sound_system import play_fire_sound
import threading
import sys

# config encoding
config = (colour_encoding, seq_encoding)

# Threading for sound
with_sound = True
if with_sound == True:
    sound_thread = threading.Thread(target=play_fire_sound, daemon=True)
    sound_thread.start()

try:
    animate_sequence(seconds=60, config=config, fps=10)
except KeyboardInterrupt:
    print("EXIT")  # TODO: make this a logging function
    sys.exit()
