''' A program to create an array of random integer numbers as a numpy array, 
    and do the following:
    #sort them and perform operations such as reshaping of the array into matrix of feasible dimensions.
    #(e.g., if we have an array of 1 * 10, then we can reshape it into 2 * 5 or 5 * 2 matrix.)
'''

import numpy as np


# Generate an array of 10 random integers between 0 and 100
Array = np.random.randint(0,100,size=10)

# Sort the array in ascending order
Sort_array = np.sort(Array)

# Reshape the sorted array into a 2x5 matrix
Matrix_2_5 = Sort_array.reshape(2,5)

# Reshape the sorted array into a 5x2 matrix
Matrix_5_2 = Sort_array.reshape(5,2)

# Print the original array
print("Original array: ")
print(Array)

# Print the sorted array
print("\nSorted array: ")
print(Sort_array)

# Print the reshaped 2x5 matrix
print("\nReshaped matrix (2x5): ")
print(Matrix_2_5)

# Print the reshaped 5x2 matrix
print("\nReshaped matrix (5x2): ")
print(Matrix_5_2)