from setuptools import setup, find_packages

# Read the requirements.txt file
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="terminal-fire",
    version="1.0.0",
    description="A terminal-based fire animation using numpy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Bram Bolt",
    author_email="contact@brambolt.me",
    url="https://github.com/bram-bolt/terminal-fire",
    packages=find_packages(),
    install_requires=install_requires,  # Automatically read from requirements.txt
    entry_points={
        "console_scripts": [
            "terminal-fire=app.main:main",
        ],
    },
)
