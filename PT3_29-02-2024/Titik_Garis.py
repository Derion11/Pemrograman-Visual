

import numpy as np
import matplotlib.pyplot as plt

#The user informs the coordinates of two points for the line
y1 = 600
x1 = 200
y2 = 200
x2 = 600

#The use decides the points' vertex diameter and color
pd = int(6); pr = 255; pg = 255; pb = 0
#pd = int(40); pr = 0, pg = 0; pb = 150
# The user decide the line width and color
lw = int(6); lr = 255; lg = 255; lb = 0
#lw = int(40); lr = 220, lg = 220; lb = 220

#Setting the size of the canvas
col = int(800)
row = int(800)
print('col, row =', col, ',', row)

#FUNCTION UNTUK MEMBUAT GARIS
## Once x and y known, create a circle and color it red.
def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16) #Preparing the black canvas
    hd = int(pd/2)                  #Calculate the half print diameter.
    hw = int(lw/2)                  #Calculate the half line width.
    dy = y2 - y1
    dx = x2 - x1

    # Draw the first point.
    for i in range(x1 - hd, x1 + hd):
        for j in range (y1 - hd, y1 + hd):
            if ((i-x1) ** 2 + (j - y1)** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Draw the second point
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i-x2) ** 2 + (j - y2)** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Garis cenderung horizontal
    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i-x1) + y1)
            x = i
            y = j
            print('x, y =', x, ',', y)
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw):
                    if ((i-x) ** 2 + (j - y)** 2) < hw **2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    ''''''
    # Garis cenderung vertikal
    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(my * (j-y1) + x1)
            x = i
            y = j
            print('x, y =', x, ',', y)
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw):
                    if ((i-x) ** 2 + (j - y)** 2) < hw **2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    
    return Gambar

## MAIN PROGRAM
hasil = buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(hasil)
plt.show()