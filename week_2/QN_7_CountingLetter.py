'''A program that prompts the user to enter a list of names and store them in a list. 
The program then will display how many times the letter 'a appears within the list.'''

Name_Lst = [] 
name = input("Enter the names separated by a comma : ")
names= name.split(",") #Separating the string to make a list

for i in names: # Looping through the list to remove the space and make it lower case
    i = i.strip().lower()
    Name_Lst.append(i) # Adding the names to the list
    print("The list of names is: ", Name_Lst) # Displaying the list of names

    count = 0 # Initializing the count variable to zero

    for j in Name_Lst: # Looping through the list to count the number of a in the list
        count += j.count('a') # Counting the number of 'a' in the list
    print("The letter 'a' appears", count, "times in the list.") # Displaying


