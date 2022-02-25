from __future__ import division, print_function
import numpy as np


def calculate_convolve(signal, n=5):
    return np.convolve(signal, np.ones((n,)) / n, mode='valid')
