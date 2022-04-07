from __future__ import division, print_function
import numpy as np
import pylab as plt
from scipy.spatial.distance import pdist, squareform

from utils.convolve import calculate_convolve

# ----------------- Plot config --------------------------------------- #
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

plt.rcParams["font.family"] = "Times", "Times New Roman", "serif"


# --------------------------------------------------------------------- #

def save_plot():
    left = 0.2
    right = 0.9
    bottom = 0.1
    top = 0.9
    wspace = 0.2
    hspace = 0.1

    plt.subplots_adjust(left, bottom, right, top, wspace, hspace)
    plt.savefig('results/1D_to_2D.jpg', bbox_inches='tight')


class RecurrencePlot(object):
    def __init__(self, row=2, col=2):
        self.signal = []

        # config pylab config for plot
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
        ax = plt.subplot(int('%s%d' % (self.size, cell)))
        ax.grid(color='gray', linestyle='dotted', linewidth=0.5)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        plt.plot(x, 'm', linewidth=1, ) if is_signal else plt.imshow(x)
        plt.title(title)
        plt.grid(grid)

    def setup_plot(self, cell=1, signal_name='Raw Signal', image_name='2D Image'):
        # plot with various axes scales
        self.subplot(self.signal, cell=cell, title=signal_name)
        self.subplot(self.recurrence_plot(), is_signal=False, cell=cell + 1, title=image_name)


if __name__ == "__main__":
    # This is an example of how to give a signal to class `RecurrencePlot`.
    # The input signal can be like [-1, 0.5, 1, ... ,1.5].

    fig = plt.figure(figsize=(8, 2))
    rp = RecurrencePlot(row=1, col=2)

    # This is how I generated a signal with a length of 50.
    raw_signal = np.random.uniform(-1, 1, 50)

    # Then I got the convolve signal. I finally drew it.
    convolved_signal = calculate_convolve(raw_signal)
    rp.set_signal(convolved_signal)

    # cell value must be odd number. You can create your own `setup_plot`
    # subplot 11(1 | 2)
    rp.setup_plot(cell=1, signal_name='Input Signal', image_name='2D image of Input Signal')

    save_plot()
