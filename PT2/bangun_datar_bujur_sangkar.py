# Kode sumber dari StackOverflow
from matplotlib import pyplot as plt, patches

plt.rcParams["figure.figsize"] = [5.00, 5.00]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(111)
rectangle = patches.Rectangle((1, 0), 3, 3,
facecolor="gray", linewidth=7)
ax.add_patch(rectangle)
rx, ry = rectangle.get_xy()
cx = rx + rectangle.get_width()/2.0
cy = ry + rectangle.get_height()/2.0
ax.annotate("This is my first GUI", (cx, cy), color='blue', weight='normal', fontsize=10, ha='center', va='center')
plt.xlim([0, 5])
plt.ylim([0, 5])
plt.show()