''' A program to create a number guessing game for the user.
'''
import random

generated_number=random.randint(1,10)

for i in range(5,0,-1):
 try:
    User_guess=int(input("guess the number between 1 and 10: "))

    if User_guess<1 or User_guess>10:
        print(" only Enter a number between 1 and 10")
        continue

    if User_guess==generated_number:
        print("you guessed it correct")
        break

    elif User_guess>generated_number:
        print(f"""you guessed wrong. you have {i-1} tries left
        The number is lower than your current guess""")

    elif User_guess<generated_number:
        print(f"""you guessed wrong. you have {i-1} tries left
        The number is greater than your current guess""")

 except ValueError:
     print("Enter a valid number")
     continue
      
else:
        
    print("you lost the game. sad, please try again")
    print(f"the number was {generated_number}")


    