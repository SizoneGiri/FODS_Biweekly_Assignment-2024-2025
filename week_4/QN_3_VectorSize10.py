''' A program to create a vector of size 10 with values ranging from 0 to 1, both excluded.'''


import numpy as np


# This will result in a vector with 8 elements, starting from the second element (index 1) to the second last element (index 8)
Vector = np.linspace (0,1,10)[1:-1] 

# Prints the resulting vector
print(f"The vector of 8 elements between 0 and 1 (excluding 0 and 1) is {Vector}")