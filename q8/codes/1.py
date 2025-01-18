import ctypes

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
categories = [1, 2, 3, 4, 5, 6, '>6']
frequencies = [results[i] for i in range(7)]
probabilities = [freq / trials for freq in frequencies]

# Generate a textual stem-and-leaf plot using probabilities
print("Stem-and-Leaf Plot (Probabilities):")
for i, prob in enumerate(probabilities[:-1]):  # Skip the '>6' category for stem-and-leaf
    stars = int(prob * 100)  # Convert probabilities into a scaled number of stars (e.g., 0.20 -> 20 stars)
    print(f"{categories[i]} | {'*' * stars}")

# Handle the ">6" category separately (if necessary)
if probabilities[-1] > 0:
    stars = int(probabilities[-1] * 100)
    print(f">{categories[-2]} | {'*' * stars}")

