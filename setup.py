from setuptools import setup, find_packages

# Read the requirements.txt file
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="terminal-fire",
    version="1.1.0",
    description="A terminal-based fire animation using numpy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Bram Bolt",
    author_email="contact@brambolt.me",
    url="https://github.com/bram-bolt/terminal-fire",
    packages=find_packages(),
    install_requires=install_requires,  # Automatically read from requirements.txt
    include_package_data=True,  # <-- This ensures non-code files are included
    entry_points={
        "console_scripts": [
            "terminal-fire=terminal_fire.src.main:main",
        ],
    },
    package_data={
        "terminal_fire": ["src/sounds/fire_sound_demo.mp3"],  # Include sound files
        # Add other non-Python files as needed
    },
)
