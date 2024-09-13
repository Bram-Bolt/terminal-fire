import random
import time
import os
from termcolor import colored

color_map = {
    "x": "red",
    "o": "blue",
    " ": None 
}

def frame_reducer(new_particle, old_particle, prob):
    return new_particle if random.random() < prob else old_particle

def color_char(char):
    return colored(char, color_map[char]) if color_map[char] else char

class FrameColumn:
    def __init__(self, height):
        self.frame = [" "] * height

    def update(self, particle):
        self.frame = [particle] + self.frame[:-1]

    def reduce_frame(self, start, prob, updated_particle):
        for i in range(start, len(self.frame)):
            self.frame[i] = frame_reducer(updated_particle, self.frame[i], prob)

    def get_colored_frame(self):
        return "".join(color_char(c) for c in self.frame)

def clear_screen():
    os.system("clear")

def display_frame(h, canvas, step):
    for j in range(h-1, -1, -1):
        row = "".join(color_char(col.frame[j]) for col in canvas)
        print(f"|{row}| {step}")

def main():
    h, w = 30, 50
    total_frames = 500
    threshold =  0.1
    updated_particle = "x"
    start = 10
    canvas = [FrameColumn(h) for _ in range(w)]

    for i in range(total_frames):
        for frame_col in canvas:
            frame_col.update("x")
            frame_col.reduce_frame(start, threshold, updated_particle)

        clear_screen()
        display_frame(h, canvas, i + 1)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
