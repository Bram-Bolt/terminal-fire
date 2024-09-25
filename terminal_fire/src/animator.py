#### OLD
from .frame import Frame
import os
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


def animate_sequence(clear_method=0, seconds=-1, config=None, fps=10):
    if clear_method == 0:
        animate_sequence_clear(seconds=seconds, config=config, fps=fps)

    elif clear_method == 1:
        animate_sequence_buffer(seconds=seconds, config=config, fps=fps)

    elif clear_method == 2:
        animate_sequence_top(seconds=seconds, config=config, fps=fps)
    elif clear_method == 3:
        animate_sequence_top_buffer(seconds=seconds, config=config, fps=fps)


# with clearing
def animate_sequence_clear(seconds=-1, config=None, fps=10):
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


## with to top + buffering
def animate_sequence_buffer(seconds=-1, config=None, fps=10):
    """Animates the sequence for a specified amount of seconds and fps"""
    height, width = get_terminal_size()
    canvas = Frame(height, width, config)

    seconds = (60 * 60 * 24) if seconds < 0 else seconds
    n_frames = int(seconds * fps)
    clear_command = "cls" if os.name == "nt" else "clear"

    for i in range(n_frames):
        # Dynamically adjust the frame to terminal size if changed
        new_height, new_width = get_terminal_size()
        if (height, width) != (new_height, new_width):
            canvas = Frame(
                new_height, new_width, config
            )  # Reinitialize canvas if size changes
            height, width = new_height, new_width

        # Move cursor to top instead of clearing the screen
        os.system(clear_command)

        # Use buffering: write everything to memory before flushing to terminal
        buffer = str(canvas)  # Generate the entire frame
        sys.stdout.write(buffer)  # Write the entire frame to stdout at once
        sys.stdout.flush()  # Ensure the buffer is flushed to the terminal at once

        # Advance the animation
        canvas.shift_frame()
        canvas.age_frame()

        # Wait for the next frame
        time.sleep(1 / fps)


## with to top
def animate_sequence_top(seconds=-1, config=None, fps=10):
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

        # Render the frame
        print(canvas)

        # Advance the animation
        canvas.shift_frame()
        canvas.age_frame()

        # Wait for the next frame
        time.sleep(1 / fps)


## with to top + buffering
def animate_sequence_top_buffer(seconds=-1, config=None, fps=10):
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
