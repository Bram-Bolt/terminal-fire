import random
particles = ["x", " "]
import sys
import time 
import os

# ANSI escape codes for colors
RED = '\033[91m'
RESET = '\033[0m'


def frame_reducer(x, prob):
    c = (random.randint(1,100))/100
    if c < prob:
        return " "
    return x

class FrameRow:
    def __init__(self, length):
        self.frame = [" "]*length

    def update(self, particle):
        self.frame = [particle] + self.frame[:-1]

    # def __repr__(self):
    #     # return "-" + "".join(self.frame) + "-"
    #     return str(self.frame)
    
    def reduce_frame(self, start, prob):
        for i in range(start, len(self.frame)):
            self.frame[i] = frame_reducer(self.frame[i], prob)
    

height = 40
width = 100
canvas = [FrameRow(height) for _ in range(width)]

frame_list = canvas.copy()

particle = "x"


def print_animation(length, reduce_start, reduce_prob):
    for i in range(length):
        # Update and reduce each frame row
        rows = []
        for frame_row in frame_list:
            frame_row.update("x")
            frame_row.reduce_frame(reduce_start, reduce_prob)
            rows.append(frame_row)

        cols = []
        for j in range(len(rows[0].frame)):  
            col_str = ""
            for row in rows:
                col_str += row.frame[j]
            cols.append(col_str)

        # manipulate elements 
        for k in range(len(cols)):
            cols[k] = cols[k].replace('x', f'{RED}x{RESET}')
                
        # Print the frame from bottom to top
        for col in reversed(cols):
            print(col)
            
        time.sleep(0.1)
        os.system("clear")
        
print_animation(500, 10, 0.1)