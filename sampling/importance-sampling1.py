import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
from scipy.stats import norm

a = 5.0

f = norm.pdf
h = lambda x: x > a
y = lambda x: h(x) * f(x)

I1 = scipy.integrate.quad(f, a, np.inf)[0]
I2 = scipy.integrate.quad(y, -np.inf, np.inf)[0]
print("scipy.integrate:", I1, I2)

N = 1000

x = norm.rvs(size=N)
I = np.mean(h(x))
print("normal monte carlo integration:", I)

g = norm(loc=5, scale=1).pdf
x = norm(loc=5, scale=1).rvs(size=N)
I = np.mean(f(x) / g(x) * h(x))
print("importance sampling:", I)

plt.subplot(211)
ix = np.arange(-5, 15, 0.01)
plt.plot(ix, f(ix), label="f(x)")
plt.plot(ix, g(ix), label="g(x)")
plt.plot(ix, h(ix), label="h(x)")
plt.xlim((-5, 15))
plt.ylim((0, 2))
plt.legend(loc="best")

plt.subplot(212)
plt.plot(ix, y(ix), label="h(x)*f(x)")
plt.xlim((4.9, 7))
plt.legend(loc="best")
#plt.show()
