import matplotlib.pyplot as plt
import numpy as np
from recurrence.plotting import setup_plot, save_plot
from recurrence.convolve import calculate_convolve

if __name__ == "__main__":
    # Example usage
    fig = plt.figure(figsize=(8, 2))

    # Configuration
    row, col = 1, 2
    size = f"{row}{col}"

    # Generate raw signal
    raw_signal = np.random.uniform(-1, 1, 50)

    # Process the signal
    convolved_signal = calculate_convolve(raw_signal)

    # Plot signals and recurrence plot
    setup_plot(
        signal=convolved_signal,
        size=size,
        cell=1,
        signal_name='Input Signal',
        image_name='2D Image of Signal'
    )

    # Save the plot
    save_plot(filepath='results/1D_to_2D.jpg')
