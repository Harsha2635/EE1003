import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
coin_toss = ctypes.CDLL('./c1.so')

# Set argument and return types for the C function
coin_toss.calculate_probabilities.argtypes = [
    ctypes.c_int,                   # int n (number of trials)
    ctypes.POINTER(ctypes.c_double), # double* probabilities
    ctypes.POINTER(ctypes.c_double)  # double* cdf
]

# Parameters
num_trials = 100000
probabilities = (ctypes.c_double * 4)()
cdf = (ctypes.c_double * 4)()

# Call the C function
coin_toss.calculate_probabilities(num_trials, probabilities, cdf)

# Convert results to Python lists
probabilities = np.array(list(probabilities))
cdf = np.array(list(cdf))

# Plotting the stem plot for probabilities
outcomes = ['0 Tails', '1 Tail', '2 Tails', '3 Tails']
plt.figure(figsize=(8, 6))
plt.stem(outcomes, probabilities, basefmt=" ", use_line_collection=True)
plt.title('Probability Distribution of Tails in 3 Coin Tosses')
plt.xlabel('Number of Tails')
plt.ylabel('Probability')
plt.grid(True)
plt.show()

