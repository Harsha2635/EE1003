import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load the shared library
one_die_sim = ctypes.CDLL('./c.so')

# Set up the C function's argument and return types
one_die_sim.roll_one_die.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]

# Parameters
trials = 10000
results = (ctypes.c_int * 7)()  # Results array for numbers 1-6 and ">6"

# Call the C function
one_die_sim.roll_one_die(trials, results)

# Extract results and calculate probabilities
categories = ['1', '2', '3', '4', '5', '6', '>6']
frequencies = [results[i] for i in range(7)]
probabilities = [freq / trials for freq in frequencies]

# Plot the probability distribution
plt.bar(categories, probabilities, color='skyblue')
plt.title("Probability Distribution of Single Die Rolls")
plt.xlabel("Die Outcome")
plt.ylabel("Probability")
plt.ylim(0, 1)  # Set y-axis to range from 0 to 1 for clarity
plt.show()

