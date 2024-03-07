import matplotlib.pyplot as plt
import numpy as np


# Menentukan wilayah (domain) diagram Cartesius dan rasio lebar dan tinggi diagram 
x = np.linspace(-3,3,10000)
plt.figure(figsize=(3,40))


# Gambar lingkaran kecil (titik) pada(0,0)
plt.plot(x, (0.01-x**2)**0.5,       '-k')
plt.plot(x, -((0.01-x**2)**0.5),    'k')

# Tentukan persamaan matematika yang diinginkan

y      = x - x - 0
y1     = -x**3 + 2*x**2 + x - 2

plt.plot(x, y,      '-k')
plt.plot(x, y1,     '-r', label='y1')
plt.legend(loc='upper left')
plt.grid()
plt.show()