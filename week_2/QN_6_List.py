'''A program that prompts the user for a series of integers and stores in a list only the values between 1-100,
   and displays the resulting list.'''

Num = input ("Enter the numbers separated by comma : ")
Number =Num.split(",") #splits the numbers into each element
Numbers =[] #empty list to store the numbers between 1-100
for nums in Number:
    #checking if the input is number or a letter
    if nums.isdigit():
        i = int(nums)
        #checking whether number is from 1-100
        if i >=1 and i<=100:
            Numbers.append(i) #appending the number to the list if it is between 1-100
        else:
         print ("Please enter a number from 1-100")
         break #if the number is not between 1-100, it will print this message
    else:
        print (f"{nums} is not a valid integer.") #if the input is not a number, it will print this message

print (f"The numbers between 1-100 are {Numbers}") #printing the list of numbers between 1-10