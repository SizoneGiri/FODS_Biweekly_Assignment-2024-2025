'''A program to create a 5x5 matrix with row values ranging from 0 to 4'''

import numpy as np

# Create a 5x5 matrix with values ranging from 0 to 24
Matrix = np.arange(25).reshape(5,5) 

# Perform the modulo operation on each element of the matrix, 
# keeping only the remainder when divided by 5
# This will result in a matrix with values ranging from 0 to 4
Matrix = Matrix % 5 

# Print the resulting 5x5 matrix with values 0-4
print(f"The 5x5 matrix with values 0-4 is \n {Matrix}")