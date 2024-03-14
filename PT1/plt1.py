# Sumber kode sample dari matplotlib.org
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19681)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('x Axis label')
ax.set_ylabel('y Axis label')

plt.show()