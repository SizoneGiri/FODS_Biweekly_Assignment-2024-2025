'''A program to create three dictionaries:
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
#dic3 = {5:50, 6:60}
and do the following tasks:
(a) Write code to concatenate these dictionaries to create a new one.
 Create a variable called nums to store the resulting dictionary.
(b) Write code to add a new key/value pair to the dictionary nums: (7, 70)
(c) Write code to update the value of the item with key 3 in nums to 80
(d) Write code to remove the third item from dictionary nums.
(e) Write code to sum all the items in the dictionary nums
(f) Write code to multiply all the items in the dictionary nums
(g) Write code to retrieve the maximum and minimum values in nums'''

# Define three dictionaries
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}

# Create an empty dictionary to store the concatenated result
combined_dict = {} 

# Add items from dict1, dict2, and dict3 to combined_dict
combined_dict.update(dict1) 
combined_dict.update(dict2)
combined_dict.update(dict3)
print(f"The concatenated dictionary: {combined_dict}")

# Add a new key-value pair to combined_dict
combined_dict[7] = 70 
print(f"Dictionary after adding new key and value: {combined_dict}")

# Update the value of key 3 in combined_dict
combined_dict[3] = 80 
print(f"Dictionary after updating the key 3 value to 80: {combined_dict}")

# Remove the item with key 3 from combined_dict
combined_dict.pop(3)
print(f"Dictionary after removing the third item: {combined_dict}")

# Calculate the sum of all values in combined_dict
total_sum = 0
for value in combined_dict.values(): 
  total_sum += value
print(f"The total sum of all items: {total_sum}")

# Calculate the product of all values in combined_dict
total_product = 1
for value in combined_dict.values(): 
  total_product *= value
print(f"The total product of all items: {total_product}")

# Find the maximum and minimum values in combined_dict
max_value = max(combined_dict.values())
min_value = min(combined_dict.values())
print(f"Maximum Value: {max_value}\nMinimum Value: {min_value}")