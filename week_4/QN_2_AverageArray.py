'''A program to ask the user to input two numbers a, b. 
and generates a random array of shape (a, b) and
prints the array and avg of the array'''

import numpy as np

# Prompts the user to input the number of rows for the array
a = int(input("Enter the number of rows for the array: "))

# Prompts the user to input the number of columns for the array
b = int(input("Enter the number of columns for the array: "))

# Generates a 2D array with random integers between 0 and 100, 
# with the shape specified by the user's input for rows (a) and columns (b)
random_array = np.random.randint(0,100, size=(a,b))

# Prints the generated random array
print(random_array)

# Calculates the average value of all elements in the array
Average = np.mean(random_array)

# Prints the calculated average value
print(f"The average value of the array is {Average}")