"""
based on http://aidiary.hatenablog.com/entry/20140728/1406555863
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import scipy.integrate

a, b = -1, 1
f = lambda x: x ** 2

x = np.linspace(-1.5, 1.5, 1000)
y = f(x)
#plt.plot(x, y)

ix = np.arange(a, b, 0.001)
iy = f(ix)
verts = [(a, 0)] + list(zip(ix, iy)) + [(b,0)]
#poly = plt.Polygon(verts, facecolor='0.8', edgecolor='k')
#plt.gca().add_patch(poly)

sci_I = scipy.integrate.quad(f, a, b)[0]
print("scipy.integrate:", sci_I)

# monte carlo

diff_result = []

for N in range(0, 100000, 100):
    x = uniform(loc=a, scale=b-a).rvs(size=N)
    mc_I = (b - a) * np.mean(f(x))
    print("monte-carlo:", mc_I)
    diff = abs(sci_I - mc_I)
    print("diff:", diff)
    diff_result.append(diff)

# lets see how accurate monte carlo is
plt.plot(diff_result)

plt.show()
