# type ignore for vscode bugs
import numpy as np  # type: ignore


def generate_normal_array(mean, length, std_dev):
    # Generate an array of x-values centered around `mean`
    x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, length)

    # Calculate the PDF values for these x-values
    y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(
        -0.5 * ((x - mean) / std_dev) ** 2
    )

    return y
