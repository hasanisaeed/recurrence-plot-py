from __future__ import division, print_function
import numpy as np
import pylab
from scipy.spatial.distance import pdist, squareform


def calculate_convolve(signal, n=5):
    return np.convolve(signal, np.ones((n,)) / n, mode='valid')


def recurrence_plot(signal, eps=0.10, steps=3):
    _2d_array = signal[:, None]
    # Pairwise distances
    distance = pdist(_2d_array)
    print(distance)
    distance = np.floor(distance / eps)
    print(distance)
    distance[distance > steps] = steps
    print(distance.shape)
    return squareform(distance)


if __name__ == "__main__":
    raw_signal = np.random.uniform(-1, 1, 1000)
    convolved_signal = calculate_convolve(raw_signal)

    pylab.title("Raw Signal")
    pylab.subplot(211)
    pylab.plot(convolved_signal)
    pylab.title("2D Image")
    pylab.subplot(212)

    pylab.imshow(recurrence_plot(convolved_signal))
    pylab.savefig('a.jpg')
