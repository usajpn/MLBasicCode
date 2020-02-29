import numpy as np
import matplotlib.pyplot as plt

def gaussian_kernel(x):
    #gk = (1 / np.sqrt(2 * np.pi)) * np.exp(-1 * (x ** 2) / 2)
    gk = (1 / np.sqrt(2 * np.pi)) * np.exp(-1 * (x ** 2) / 2)
    return gk

def main():
    x = np.linspace(-5, 5, 10000)
    y = [gaussian_kernel(i) for i in x]

    s = (10/10000) * np.array(y)

    s = np.sum(s)
    print(s)

    plt.plot(x, y)
    plt.show()

main()
