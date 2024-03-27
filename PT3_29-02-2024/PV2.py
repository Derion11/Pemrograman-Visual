import matplotlib.pyplot as plt

y = 10  # y-coordinate of the horizontal line
xmin = 0.25  # Starting x-coordinate
xmax = 0.75  # Ending x-coordinate

# Plot the horizontal line from xmin to xmax
plt.axhline(y, xmin=xmin, xmax=xmax, color='purple')

# Set the x and y axis limits
plt.xlim(0, 15)
plt.ylim(0, 15)

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Horizontal Line from x=0.25 to x=0.75')

# Set the background color to black
plt.gca().set_facecolor('black')

# Display the plot
plt.show()