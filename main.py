from __future__ import division, print_function
import numpy as np
import pylab as plt
from scipy.spatial.distance import pdist, squareform

from utils import calculate_convolve


# ----------------- Plot config -------------------------------------------
SMALL = 8
MEDIUM = 10
BIGGER = 11

plt.rc('font', size=SMALL)          # controls default text sizes
plt.rc('axes', titlesize=SMALL)     # font size of the axes title
plt.rc('axes', labelsize=MEDIUM)    # font size of the x and y labels
plt.rc('xtick', labelsize=SMALL)    # font size of the tick labels
plt.rc('ytick', labelsize=SMALL)    # font size of the tick labels
plt.rc('legend', fontsize=SMALL)    # legend font size
plt.rc('figure', titlesize=BIGGER)  # font size of the figure title
# -------------------------------------------------------------------------


class RecurrencePlot(object):
    def __init__(self, signal, row=2, col=2):
        self.signal = signal
        self.size = '%d%d' % (row, col)

    def recurrence_plot(self, eps=0.10, steps=3):
        _2d_array = self.signal[:, None]

        # Pairwise distances
        distance = pdist(_2d_array)
        distance = np.floor(distance / eps)
        distance[distance > steps] = steps
        return squareform(distance)

    def subplot(self, x, is_signal=True, index=1, title=None, grid=True):
        plt.subplot(int('%s%d' % (self.size, index)))
        plt.plot(x) if is_signal else plt.imshow(x)
        plt.title(title)
        plt.grid(grid)

    def save(self):
        # plot with various axes scales
        plt.figure()
        self.subplot(self.signal, index=1, title='Raw Signal')
        self.subplot(self.recurrence_plot(), is_signal=False, index=2, title='2D Image')
        self.subplot(self.signal, index=3, title='Raw Signal')
        self.subplot(self.recurrence_plot(), is_signal=False, index=4, title='2D Image')
        plt.savefig('result.jpg')


if __name__ == "__main__":
    raw_signal = np.random.uniform(-1, 1, 500)
    convolved_signal = calculate_convolve(raw_signal)
    rp = RecurrencePlot(convolved_signal)
    rp.save()
