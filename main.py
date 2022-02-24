from __future__ import division, print_function
import numpy as np


def calculate_convolve(s, r=20):
    print(np.ones((r,)) / 1)
    return np.convolve(s, np.ones((r,)) / r, mode='valid')


if __name__ == "__main__":
    ru = [1, 2, 3]
    ru_filtered = calculate_convolve(ru)
