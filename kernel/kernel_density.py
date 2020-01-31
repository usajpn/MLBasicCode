"""
Very very simple kernel density estimator
"""


import numpy as np
import matplotlib.pyplot as plt


class KernelDensityEstimator():
    def __init__(self, samples, bandwidth):
        self.samples = samples
        self.bandwidth = bandwidth

    def gaussian_kernel(self, x):
        gk = (1 / np.sqrt(2 * np.pi)) * np.exp(-1 * (x ** 2) / 2)
        return gk

    def predict(self, x_test):
        n = len(self.samples)
        h = self.bandwidth

        prob = np.zeros(x_test.size)
        for i, x in enumerate(x_test):
            for s in self.samples:
                prob[i] += self.gaussian_kernel((x - s) / h)
        prob = 1 / (n * h) * prob
        return prob

def main():
    samples = [3.4, 2.1, 1.2, 2.4, 2.1, 2.3, 3.0, 4.6]
    samples = np.array(samples)
    bandwidth = 0.5

    # set up the samples as training data
    kde = KernelDensityEstimator(samples, bandwidth)

    x = np.linspace(0, 10, 100)
    plt.plot(x, kde.predict(x))
    plt.show()

main()
