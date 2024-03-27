import matplotlib.pyplot as plt

x = [25, 175]
y = [25, 175]
colors = ['red', 'green']

for i in range(len(x)):
    plt.plot(x[i], y[i], 'o', color=colors[i])

plt.axis((0, 200, 0, 200))
plt.show()