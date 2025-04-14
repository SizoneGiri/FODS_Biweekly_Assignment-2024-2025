'''write a Python program that accepts a string and calculates the number of digits and letters.'''

string=input("Enter a string containing letter or digits: ")
number_of_digits=0
number_of_letters=0

for chr in string:
    if chr.isnumeric():
     number_of_digits+=1
    elif chr.isalpha():
     number_of_letters+=1
print(f"number of letters= {number_of_letters} and number of digits= {number_of_digits}")