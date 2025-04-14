
'''A program that accepts a string and calculates the number of lower case and upper case letters'''

#function to calculate lowercase and uppercase
def case(Word):
    upper = sum(1 for char in Word if char.isupper())
    lower = sum(1 for char in Word if char.islower())
    return upper, lower

#input from user
Word=input("enter a word and ill count the uppercase and lower case ")
Upper, Lower=case(Word)

#displaying the result
print(f"The word contains {Upper} uppercase letters and {Lower} lowercase letters") 