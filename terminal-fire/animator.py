from frame import Frame
import os
import time


def animate_sequence(seconds, height, width, config):
    canvas = Frame(height, width, config)
    n_frames = seconds * 10
    for i in range(n_frames):
        print(canvas)
        canvas.shift_frame()
        canvas.age_frame()
        time.sleep(0.1)
        os.system("clear")
