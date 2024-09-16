from setuptools import setup, find_packages

setup(
    name="terminal-fire",
    version="0.0.3",
    description="A terminal-based fire animation using numpy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Bram Bolt",
    author_email="contact@brambolt.me",
    url="https://github.com/bram-bolt/terminal-fire",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "terminal-fire=app.main:main",
        ],
    },
)
