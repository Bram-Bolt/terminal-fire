import os
import pygame


def play_fire_sound():
    # Get the current file's directory (app directory)
    current_dir = os.path.dirname(__file__)
    sound_path = os.path.join(current_dir, "sounds", "fire_sound_demo.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)
