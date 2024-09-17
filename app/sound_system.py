import time
from playsound import playsound
from pathlib import Path


# TODO: fire sound effect that sounds like fire not water
def play_fire_sound():
    sound_path = Path("app/sounds/fire_sound_demo.mp3")
    """plays the fire sound"""
    while True:
        playsound(sound_path)
