#### OLD
from .frame import Frame
import time
import sys
import shutil  # For getting terminal size dynamically


# TODO: make better start-up animation!


def get_terminal_size():
    """Returns the current terminal width and height."""
    size = shutil.get_terminal_size()
    return size.lines, size.columns  # height, width


def move_cursor_to_top():
    """Move the cursor to the top of the terminal."""
    print("\033[H", end="")  # ANSI escape code to move the cursor to the top


## with to top + buffering
def animate_sequence(seconds=-1, config=None, fps=10):
    """Animates the sequence for a specified amount of seconds and fps"""
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

        # Move cursor to top instead of clearing the screen
        move_cursor_to_top()

        # Use buffering: write everything to memory before flushing to terminal
        buffer = str(canvas)  # Generate the entire frame
        sys.stdout.write(buffer)  # Write the entire frame to stdout at once
        sys.stdout.flush()  # Ensure the buffer is flushed to the terminal at once

        # Advance the animation
        canvas.shift_frame()
        canvas.age_frame()

        # Wait for the next frame
        time.sleep(1 / fps)
