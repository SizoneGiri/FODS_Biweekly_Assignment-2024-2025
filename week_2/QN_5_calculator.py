''' A calculator program that takes a string of numbers and performs the following functions
 A. Addition
 B. Subtraction
 C. Multiplication
 D. Division
 E. Truncated division
 F. Modulus
 G. Exponentiation'''

#Addition function
def Addition (a,b):
    Add = a + b
    return Add

#Subtraction function
def Subtraction (a,b):
    Sub = a - b
    return Sub

#Multiplication function
def Multiplication (a, b):
    multiply = a * b
    return multiply

#Division function
def Division (a,b):
    Quotient = a/b
    Quotient = round(Quotient,2) #round to 2 decimal places
    return Quotient

#Truncated division function
def Truncated_divison (a,b):
    quotient = a//b 
    return quotient

#Modulus function
def Modulus (a,b):
    reminder = a%b
    return reminder

#Exponentiation function
def Exponential (a,b):
    Exponential = pow(a,b) #using pow function for exponentiation
    return Exponential

#Taking input from user
num1 = int (input("Enter the first number : "))
num2 = int (input("Enter the second number : "))
#Displaying all of the outputs
print (f"The addition of {num1} and {num2} is {Addition(num1,num2)}")
print (f"The subtraction of {num1} and {num2} is {Subtraction(num1,num2)}")
print (f"The multiplication of {num1} and {num2} is {Multiplication(num1,num2)}")
print (f"The division of {num1} and {num2} is {Division(num1,num2)}")
print (f"The truncated division of {num1} and {num2} is {Truncated_divison(num1,num2)}")
print (f"The modulus of {num1} and {num2} is {Modulus(num1,num2)}")
print (f"The exponentiation of {num1} and {num2} is {Exponential(num1,num2)}")