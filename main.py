from __future__ import division, print_function
import numpy as np


def calculate_convolve(signal, r=5):
    return np.convolve(signal, np.ones((r,)) / r, mode='valid')


if __name__ == "__main__":
    signal = [1, 2, 3]
    convolved_signal = calculate_convolve(signal)
    print(convolved_signal)
