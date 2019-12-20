import numpy as np
import matplotlib.pyplot as plt


def get_data():
    train = np.loadtxt('data.csv', delimiter=',', skiprows=1)
    train_x = train[:, 0]
    train_y = train[:, 1]

    return train_x, train_y

def plot_data(train_x, train_y):
    plt.plot(train_x, train_y, 'o')
    plt.show()

def regression():
    # init param
    theta0 = np.random.rand()
    theta1 = np.random.rand()

    # hypothesis function: f(x) = theta0 + theta1 * x
    def f(x):
        return theta0 + theta1 * x

    # cost function / loss function
    def E(x, y):
        return 0.5 * np.sum((y - f(x)) ** 2)

def preprocess(train_x):
    mu = train_x.mean()
    sigma = train_x.std()
    train_z = (train_x - mu) / sigma
    return train_z

if __name__ == "__main__":
    train_x, train_y = get_data()
    train_x = preprocess(train_x)

    plot_data(train_x, train_y)
