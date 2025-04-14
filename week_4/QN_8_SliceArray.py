'''A program to input an array of numbers from the user (at least 10 elements in list) and
   sorts them and performs slicing operations to get elements between indexes such as 2-5, 5-8, 2-9. '''

import numpy as np

# Initialize an empty list to store user input numbers
user_input_numbers = []

# Loop to collect 10 numbers from the user
for i in range(10):
  # Prompt user to enter a number and convert it to integer
  user_number = int(input(f"Enter number {i+1}: "))
  # Append the user input number to the list
  user_input_numbers.append(user_number)  # Add user input to the list

# Convert the list to a NumPy array
input_array = np.array(user_input_numbers)

# Print the original array
print(f"Original array: {input_array}")

# Sort the array in ascending order
sorted_array = np.sort(input_array)

# Print the sorted array
print(f"Sorted array: {sorted_array}")

# Perform slicing operations to extract specific elements
# Extract elements from index 2 to 5 (inclusive)
slice_2_to_5 = sorted_array[2:6]  
# Extract elements from index 5 to 8 (inclusive)
slice_5_to_8 = sorted_array[5:9]
# Extract elements from index 2 to 9 (inclusive)
slice_2_to_9 = sorted_array[2:10]

# Print the sliced elements
print(f"Elements between 2-5: {slice_2_to_5}")
print(f"Elements between 5-8: {slice_5_to_8}")
print(f"Elements between 2-9: {slice_2_to_9}")