import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Coordinates of the first triangle
pts1 = np.array([[2,2], [2,5], [5,2]])
p1 = Polygon(pts1, facecolor='gray')

# Coordinates of the second triangle
pts2 = np.array([[2,5.1], [5,2.1], [5,5]])
p2 = Polygon(pts2, facecolor='gray')

# Plotting the triangles
ax = plt.gca()

ax.add_patch(p1)
# Add text inside the first triangle with fontsize
ax.text(2.25, 2.5, 'Its the best offer \nin town!', ha='left', va='center', color='blue', fontsize=10)

ax.add_patch(p2)
# Add text inside the second triangle with fontsize
ax.text(4.5, 4.5, 'i', ha='right', va='center', color='blue', fontsize=10)

ax.set_xlim(1, 7)
ax.set_ylim(1, 8)
plt.show()