''' A program to create two sets:
set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}
and do the following:
(a)  perform a union of these sets. Print the length of the resulting set.
(b)  perform an intersection of set1 and set2.
(c)  to compute the symmetric difference between set1 and set2
(d)  to add the value 40 to set1, did the set change?
(e)  to remove value 20 from set2'''

Set1 = {20, 40, 60}
Set2 = {10, 20, 30, 40, 50, 60}

combined_elements = Set2|Set1  # merging the two sets ("|" is a merge operator)
total_elements = len(combined_elements)

print(f"The combined elements of collection 1 and collection 2: {combined_elements}")
print(f"Total number of elements in the combined set: {total_elements}")

common_elements = Set1 & Set2  # "&" is a common elements operator
print(f"The common elements between collection 1 and collection 2: {common_elements}")

distinct_elements = Set1 ^ Set2  # "^" is a distinct elements operator
print(f"The distinct elements between collection 1 and collection 2: {distinct_elements}")

Set1.add(40) # adding an element to a set
print(f"Collection 1 after appending 40: {Set1}")
print("The collection didn't change after appending 40 because collections store unique values")

Set2.remove(20) # removing a value from a set
print(f"Collection 2 after deleting 20: {Set2}")