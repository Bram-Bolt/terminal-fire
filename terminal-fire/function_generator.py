# type ignore for vscode bugs
import numpy as np  # type: ignore


def generate_normal_array(mean, length, std_dev):
    """Generates a np.array following a normal distributtion"""
    x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, length)
    y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(
        -0.5 * ((x - mean) / std_dev) ** 2
    )
    return y
