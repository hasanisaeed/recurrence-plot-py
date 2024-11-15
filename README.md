# Recurrence Plot
[Recurrence Plot](https://en.wikipedia.org/wiki/Recurrence_plot) – A recurrence plot (RP) is an advanced technique of **nonlinear** data analysis. It is a visualisation (or a graph) of a square matrix, in which the matrix elements correspond to those times at which a state of a dynamical system recurs (columns and rows correspond then to a certain pair of times).

## Result
![](results/1D_to_2D.jpg)

## Usage
**1. Install requirements:**

Ensure you have Python 3 installed. Install the required dependencies using:


    pip install -r requirements.txt

**2. Run `example.py` script:**

    python3 example.py # or python example.py

This will:

- Generate a random signal.
- Smooth the signal using a moving average filter.
- Compute and visualize the recurrence plot.
- Save the resulting plot as results/1D_to_2D.jpg.

----
## How to Use the recurrence Package

If you want to use the recurrence package in your own projects:

1) **Import the Required Modules:**

    For recurrence plot functions, import from recurrence.plotting.
    For signal processing utilities, import from recurrence.convolve.

    Example:

    ```python
    from recurrence.plotting import setup_plot, save_plot
    from recurrence.convolve import calculate_convolve
    ```

2) **Process Your Signal:** 
   
   Use `calculate_convolve` to smooth your input signal, then use the `setup_plot` and `save_plot` functions to generate and save recurrence plots.