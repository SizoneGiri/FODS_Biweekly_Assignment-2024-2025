'''A program to check whether the given number is armstrong or not'''

#function to check armstrong number
def is_armstrong(n):
    temp = n
    power = len(str(n))
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    return n == total

#input from the user
number=int(input("enter a number to see if the number is armstrong or not "))

#displaying the result using if statement
if is_armstrong(number)==False:
    print("the number is not armstrong")
elif is_armstrong(number)==True:
    print("the number is armstrong")