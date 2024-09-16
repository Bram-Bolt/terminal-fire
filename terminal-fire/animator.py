from frame import Frame
import os
import time
import shutil  # For getting terminal size dynamically


def get_terminal_size():
    """Returns the current terminal width and height."""
    size = shutil.get_terminal_size()
    return size.lines, size.columns  # height, width


def animate_sequence(seconds=-1, config=None, fps=10):
    """Animates the sequence for a specified amount of seconds and fps"""
    
    height, width = get_terminal_size()

    canvas = Frame(height, width, config)
    if seconds > 0:
        n_frames = int(seconds * fps)
    else:
        # full day
        n_frames = int((60 * 60 * 24) * fps)

    for i in range(n_frames):
        # Dynamically adjust the frame to terminal size if changed
        new_height, new_width = get_terminal_size()
        if (height, width) != (new_height, new_width):
            canvas = Frame(
                new_height, new_width, config
            )  # Reinitialize canvas if size changes
            height, width = new_height, new_width

        # Render the frame
        print(canvas)

        # Advance the animation
        canvas.shift_frame()
        canvas.age_frame()

        # Wait for the next frame
        time.sleep(1 / fps)

        os.system("clear")
