import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-5, 5, 100)

# Plot y = x
plt.plot(x, x, label='y = x')

# Plot y = -x + 4
plt.plot(x, -x + 4, label='y = -x + 4')

# Plot y = 2
plt.axhline(2, color='red', label='y = 2')

# Plot x = 2
plt.axvline(2, color='green', label='x = 2')

# Set the x and y axis limits
plt.xlim(-5, 5)
plt.ylim(-1, 5)

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lines')

# Add legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()