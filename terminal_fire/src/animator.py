from .frame import Frame
import os
import time
import shutil  # For getting terminal size dynamically


def get_terminal_size():
    """Returns the current terminal width and height."""
    size = shutil.get_terminal_size()
    return size.lines, size.columns  # height, width


# TODO: make better start-up animation!
def animate_sequence(seconds=-1, config=None, fps=10):
    """Animates the sequence for a specified amount of seconds and fps"""
    clear_command = "cls" if os.name == "nt" else "clear"
    height, width = get_terminal_size()

    canvas = Frame(height, width, config)

    seconds = (60 * 60 * 24) if seconds < 0 else seconds
    n_frames = int(seconds * fps)

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

        os.system(clear_command)
