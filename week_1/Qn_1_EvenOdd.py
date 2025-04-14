'''program to take a number input from the user and display whether the number is even or odd'''


Number=int(input("enter a number "))

if Number%2==0 and Number>-1:
    print("the number is even")
elif Number%2==1 and Number>-1:
    print("the number is odd")
else:
    print("""the number you have entered is less then zero
          please enter a positive integer""")