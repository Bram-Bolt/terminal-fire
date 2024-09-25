from .animator import animate_sequence
from .colour_config import colour_encoding, seq_encoding
from .sound_system import play_fire_sound
import threading
import sys
import argparse
import logging

# add logging
logging.basicConfig(level=logging.INFO)


# CLI parsing
def parse_arguments() -> argparse.Namespace:
    """parse CLI arguments"""
    parser = argparse.ArgumentParser(
        prog="terminal-fire",
        description="Generate an ASCII fireplace in your terminal/CLI.",
        epilog="For any questions, reach out to contact@brambolt.me",
    )

    parser.add_argument(
        "-s",
        "--sound",
        dest="enable_sound",
        action="store_true",
        help="Play the fireplace with sound!",
        default=False,
    )

    parser.add_argument(
        "-c",
        "--clear",
        dest="clear_method",
        type=str,
        default="0",
        help="Clear method (default: 0)",
    )

    return parser.parse_args()


args = parse_arguments()

# config encoding
config = (colour_encoding, seq_encoding)


# Threading for sound
def main() -> None:
    """Generate an ASCII fireplace in your terminal/CLI"""
    if args.enable_sound == True:
        sound_thread = threading.Thread(target=play_fire_sound, daemon=True)
        sound_thread.start()

    try:
        animate_sequence(
            clear_method=int(args.clear_method), seconds=-1, config=config, fps=10
        )
    except KeyboardInterrupt:
        logging.info("Fire animation terminated succesfully.")
        sys.exit()


if __name__ == "__main__":
    main()
