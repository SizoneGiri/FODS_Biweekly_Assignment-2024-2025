'''A program that prompts the user to enter integer values to populate two lists,
then prints messages to determine the following:
(a) Whether the lists are of the same length.
(b) Whether the elements in each list sum to the same value.
(c) Whether there are any values that occur in both lists'''

Lst1 = input (" Enter the elements of the first list separated by a comma ").split(",") 
#Spliting the elements into individual number
Lst2 = input (" Enter the elements of the second list separated by a comma ").split(",") 
Number1= [int(num) for num in Lst1] #converting each element into integer
Number2= [int(num) for num in Lst2] #converting each element into integer
print (f"List 1: {Number1} \n List 2: {Number2}")
#checking if the lists are of the same length
if len(Number1)==len(Number2):
  print (f"List 1 and List 2 have the same length.") 
else:
  print (f" List 1 length : {len(Number1)} \nList 2 length : {len(Number2)}") 

Sum1 = 0 
Sum2 = 0 
for num in Number1: #adding the value of list 1
  Sum1+=num
for num in Number2: #adding the value of list 2
  Sum2+=num

if Sum1 == Sum2: #checking if the sum of both lists are equal
  print (f"The sum of List 1 and the sum of List 2 are equal : {Sum1}")
else:
  print (f"The sum of List 1 : {Sum1} \nThe sum of List 2 : {Sum2}")

Intersection = set(Number1) & set(Number2) #finding the common elements between the two lists
if Intersection:
  print (f"The common elements of List1 and List2 are {Intersection}") #printing the common elements
else:
  print ("List 1 and List 2 do not have any common elements") #printing the message if there are no common elements