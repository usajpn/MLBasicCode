import numpy as np
import matplotlib.pyplot as plt

def gaussian_kernel(x):
    gk = (1 / np.sqrt(2 * np.pi)) * np.exp(-1 * (x ** 2) / 2)
    return gk

def main():
    s_samples = [1.2, 2.4, 2.2, 2.6, 6.5]
    a_samples = [2.3, 4.5, 7.3, 7.8, 8.3]

    s_test = 2.0

    n_samples = len(s_samples)

    for s, a in s_samples, a_samples:
        gaussian_kernel(s)


main()
