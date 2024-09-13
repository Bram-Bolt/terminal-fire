import random
particles = ["x", " "]
import sys
import time 
import os

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

    def __repr__(self):
        return "|" + "".join(self.frame) + "|"
    
    def reduce_frame(self, start, prob):
        for i in range(start, len(self.frame)):
            self.frame[i] = frame_reducer(self.frame[i], prob)
    
frame = [" "]*50

n = 20
canvas = [FrameRow(50) for _ in range(n)]

frame_list = canvas.copy()

particle = "x"

frame[0] = particle
for i in range(500):
    for frame_row in frame_list:
        frame_row.update("x")
        frame_row.reduce_frame(0, 0.1)
        print(f"{frame_row} + {i}")
    time.sleep(0.1)
    os.system("clear")

