print("\033c")
import numpy as np
import matplotlib.pyplot as plt

# The user informs the coordinates of the two points for the line.
# a points = (100, 200)
x1 = 100
y1 = 200
# b points = (1800, 200)
x2 = 1800
y2 = 200

# The user declares the line width
lw = int(10)

# Calculate the half line width
hw = int(lw / 2)

# Setting the size of the canvas
row = int(1080)
col = int(1920)
print('col, row =', col, ',', row)

# Preparing the black canvas
gambar = np.zeros(shape=(row, col, 3), dtype=np.uint16)

# Coloring the two points red (loop, condition, comparison)
for i in range(x1 - hw, x1 + hw):
    for j in range(y1 - hw, y1 + hw):
        if ((i - x1) ** 2 + (j - y1) ** 2) < hw ** 2:
            gambar[j, i, 0] = 255

for i in range(x2 - hw, x2 + hw):
    for j in range(y2 - hw, y2 + hw):
        if ((i - x2) ** 2 + (j - y2) ** 2) < hw ** 2:
            gambar[j, i, 0] = 255

# Calculate the slope of the line
m = (y2 - y1) / (x2 - x1)

# Calculate the y-intercept
c = y1 - m * x1

# Draw the line using the equation y = mx + c
for x in range(x1, x2 + 1):
    y = int(m * x + c)
    for i in range(-hw, hw + 1):
        for j in range(-hw, hw + 1):
            gambar[y + j, x + i] = [255, 0, 0]  # Set all color channels to white

plt.figure()
plt.imshow(gambar)
plt.show()