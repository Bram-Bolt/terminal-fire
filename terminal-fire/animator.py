from frame import Frame
import os
import time


def animate_sequence(seconds, height, width, config):
    """Updates frames for a certain amount of seconds"""
    canvas = Frame(height, width, config)
    # convert frames to seconds
    n_frames = seconds * 10
    for i in range(n_frames):
        # TODO: make dynamic?
        # new_w, new_h = os.get_terminal_size()
        # if (height, width) != (new_h, new_w):
        #     canvas = Frame(height, width, config)
        #     height, width = new_h, new_w
        print(canvas)
        # print(f"frame: {i}")  # debug
        canvas.shift_frame()
        canvas.age_frame()
        time.sleep(0.1)
        os.system("clear")
