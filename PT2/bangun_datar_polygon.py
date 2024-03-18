import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Coordinates of the first polygon
pts1 = np.array([[3,2], [6,2], [7,4], [6,6], [3,6], [2,4]])
p1 = Polygon(pts1, facecolor='gray')

# Plotting the polygon
ax = plt.gca()

ax.add_patch(p1)
# Add text inside the first triangle with fontsize
ax.text(4.5, 4, 'Its the best offer in town!', ha='center', va='center', color='blue', fontsize=8)

ax.set_xlim(1, 10)
ax.set_ylim(1, 10)
plt.show()