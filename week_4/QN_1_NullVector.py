'''A program to create a null vector of size 10 but the fifth value which is 1.'''

import numpy as np 

# Creates a null vector of size 10
null_vector = np.zeros(10)

# Modify the 5th element of the null vector (at index 4, since indexing starts at 0) to 1
null_vector[4] = 1

# Print the modified null vector
print(null_vector)