from frame import Frame
import os
import time
import shutil  # For getting terminal size dynamically


def get_terminal_size():
    """Returns the current terminal width and height."""
    size = shutil.get_terminal_size()
    return size.lines, size.columns  # height, width


def animate_sequence(seconds, config=None, fps=10):
    """Animates the sequence for a specified amount of seconds, dynamically adjusting to terminal size."""
    if height is None or width is None:
        height, width = get_terminal_size()

    canvas = Frame(height, width, config)
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

        # Clear the screen using ANSI escape sequences (faster than os.system("clear"))
        os.system("clear")


# Example usage (assuming config is passed):
# animate_sequence(10, config=some_config)
