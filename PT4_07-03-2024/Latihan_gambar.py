import matplotlib.pyplot as plt
import numpy as np

'''
x^2 + y^2   = 2^2
y^2         = 4 - x^2
y           = +/- (4-x^2)^1/2 
'''

x = np.linspace(-4,4,10000)
plt.figure(figsize=(8,6.5))

# Tentukan persamaan matematika yang diinginkan
y   = x -x -0
y1  = (5-x**2)**0.5
y2  = -(5-x**2)**0.5

y3  = 2 + (2-(x-2)**2)**0.5
y4  = 2 - (2-(x-2)**2)**0.5

y5  = 2 + (2-(x+2)**2)**0.5
y6  = 2 - (2-(x+2)**2)**0.5


plt.plot(x, y,   '-k')
plt.plot(x, y1,  '-k',label='y1, y2')
plt.plot(x, y2,  '-k')
plt.plot(x, y3,  '-k',label='y3, y4')
plt.plot(x, y4,  '-k')
plt.plot(x, y5,  '-k',label='y5, y6')
plt.plot(x, y6,  '-k')


plt.legend(loc='upper center')
plt.grid()
plt.show()