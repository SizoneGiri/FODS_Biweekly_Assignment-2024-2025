"""a program that prompts the user for two integer values 
and displays the results of the first number divided by the second with exactly two decimal places displayed"""

#taking input from the user
Number_1=int(input("enter the first number "))
Number_2=int(input("enter the second number "))

#dividing the first number with the second
F_Number=float(Number_1/Number_2)

print(round(F_Number,2)) #to round up the decimals to only two digits