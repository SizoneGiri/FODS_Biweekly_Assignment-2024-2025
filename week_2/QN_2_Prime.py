'''A program to check whether the given number is prime or not.'''

#function to check if the number is prime
def prime (number):
    i=1 
    count = 0 #increases by how many times the number can be divided
    if number <=1: 
        return False
    for i in range (i,number+1):
        if number%i==0:
            count +=1
    if count >2: 
        return False
    return True
number = int(input("Enter a number: "))
#output using if statement
if prime(number):
    print(f"{number} is a Prime number ")
else: 
    print(f"{number} is not a Prime number")