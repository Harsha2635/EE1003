import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Create np.linspace for x from 1 to 3, divided into 500 points
x = np.linspace(1, 3, 500)

# Initialize y array with the same length as x
y = np.zeros_like(x)

# Set the first value of y
y[0] = 1

# Step size
h = 0.004

# Compute y values using the formula by iterating through the steps
for n in range(1, len(x)):
    y[n] = y[n-1] + ((y[n-1] - x[n-1]) / (y[n-1] + x[n-1])) * h

# Define the implicit function
def implicit_function(y, x):
    return 0.5 * np.log(y**2 / x**2 + 1) + np.arctan(y / x) + np.log(x) - (np.pi / 4 + 0.5 * np.log(2))

# Solve the implicit function for each x to find corresponding y
implicit_y = []
for xi in x:
    yi_initial_guess = 1  # Initial guess for y
    yi_solution = fsolve(implicit_function, yi_initial_guess, args=(xi,))
    implicit_y.append(yi_solution[0])

# Convert implicit_y to a numpy array
implicit_y = np.array(implicit_y)

# Plot the graph of y versus x
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y vs x (iterative)', color='blue')
plt.plot(x, implicit_y, label='Implicit function', color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

