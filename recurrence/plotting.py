import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import pdist, squareform

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

def save_plot(filepath='results/1D_to_2D.jpg'):
    """Adjust and save the plot."""
    left = 0.2
    right = 0.9
    bottom = 0.1
    top = 0.9
    wspace = 0.2
    hspace = 0.1

    plt.subplots_adjust(left, bottom, right, top, wspace, hspace)
    plt.savefig(filepath, bbox_inches='tight')

def recurrence_plot(signal, eps=0.10, steps=3):
    """Generate a recurrence plot from a 1D signal."""
    _2d_array = signal[:, None]
    distance = pdist(_2d_array)
    distance = np.floor(distance / eps)
    distance[distance > steps] = steps
    return squareform(distance)

def subplot(x, size, cell, is_signal=True, title=None, grid=True):
    """Create a subplot for the signal or image."""
    ax = plt.subplot(int(f"{size}{cell}"))
    ax.grid(color='gray', linestyle='dotted', linewidth=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    if is_signal:
        plt.plot(x, 'm', linewidth=1)
    else:
        plt.imshow(x)
    
    plt.title(title)
    plt.grid(grid)

def setup_plot(signal, size, cell, signal_name='Raw Signal', image_name='2D Image'):
    """Set up and display the plot for the signal and its recurrence plot."""
    subplot(signal, size=size, cell=cell, is_signal=True, title=signal_name)
    rp = recurrence_plot(signal)
    subplot(rp, size=size, cell=cell + 1, is_signal=False, title=image_name)
