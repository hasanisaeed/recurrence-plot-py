from __future__ import division, print_function
import numpy as np
import pylab as plt
from scipy.spatial.distance import pdist, squareform

from utils.convolve import calculate_convolve

# ----------------- Plot config -------------------------------------------
SMALL = 8
MEDIUM = 10
BIGGER = 11

plt.rc('font', size=SMALL)  # controls default text sizes
plt.rc('axes', titlesize=SMALL)  # font size of the axes title
plt.rc('axes', labelsize=MEDIUM)  # font size of the x and y labels
plt.rc('xtick', labelsize=SMALL)  # font size of the tick labels
plt.rc('ytick', labelsize=SMALL)  # font size of the tick labels
plt.rc('legend', fontsize=SMALL)  # legend font size
plt.rc('figure', titlesize=BIGGER)  # font size of the figure title
plt.rcParams["font.family"] = "Times", "Times New Roman", "serif"


# -------------------------------------------------------------------------

def save_plot():
    left = 0.125
    right = 0.9
    bottom = 0.1
    top = 0.9
    wspace = 0.2
    hspace = 0.21

    plt.subplots_adjust(left, bottom, right, top, wspace, hspace)
    plt.savefig('results/1D_to_2D.jpg', bbox_inches='tight')


class RecurrencePlot(object):
    def __init__(self, row=2, col=2):
        self.signal = []
        self.size = '%d%d' % (row, col)

    def set_signal(self, signal):
        self.signal = signal

    def recurrence_plot(self, eps=0.10, steps=3):
        # Convert 1-D signal to 2-D signal
        _2d_array = self.signal[:, None]

        # Pairwise distances
        distance = pdist(_2d_array)
        distance = np.floor(distance / eps)
        distance[distance > steps] = steps
        return squareform(distance)

    def subplot(self, x, is_signal=True, cell=1, title=None, grid=True):
        plt.subplot(int('%s%d' % (self.size, cell)))
        plt.plot(x) if is_signal else plt.imshow(x)
        plt.title(title)
        plt.grid(grid)

    def setup_plot(self, cell=1, signal_name='Raw Signal', image_name='2D Image'):
        # plot with various axes scales
        self.subplot(self.signal, cell=cell, title=signal_name)
        self.subplot(self.recurrence_plot(), is_signal=False, cell=cell + 1, title=image_name)


if __name__ == "__main__":
    fig = plt.figure(figsize=(8, 6))

    rp = RecurrencePlot()

    raw_signal = np.random.uniform(-1, 1, 50)
    convolved_signal = calculate_convolve(raw_signal)
    rp.set_signal(convolved_signal)

    # cell value must be odd number
    # subplot 22(1,2)
    rp.setup_plot(cell=1, signal_name='First Signal', image_name='2D image for first signal')

    raw_signal = np.random.uniform(-1, 1, 50)
    convolved_signal = calculate_convolve(raw_signal)
    rp.set_signal(convolved_signal)

    # subplot 22(3,4)
    rp.setup_plot(cell=3, signal_name='Second Signal', image_name='2D image for second signal')

    save_plot()
