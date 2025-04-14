"""This is a program to find the simple interest when the value of principle, rate of interest and
time period is provided by the user."""

Principle=int(input("Enter principle: "))
Rate_of_interest=int(input("Enter the rate of interest in percentage: "))
Time_Period=int(input("Enter the time period in years: "))
SimpleInterest=(Principle*Time_Period*Rate_of_interest)/100
print ("Your simple interest would be: ",SimpleInterest)