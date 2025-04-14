'''A Program with function named get_daily_temps that prompts the user for the average temperature 
 for each day of the week and returns a dictionary containing the information the user entered.'''


def daily_temps():
  """
  Prompts the user for the average temperature for each day of the week
  and returns a dictionary containing the information the user entered.
  """
  daily_temps = {}  # creating empty dictionary to store values later
  for i in range(7):  # iterates 7 times 0-6
    day = input("Enter the day of the week: ").capitalize()
    temp = float(input(f"Enter the average temperature of {day}: "))
    daily_temps[day] = temp  # this line indicates day as a key and temp as its value in daily_temps dictionary
  return daily_temps

daily_temps = daily_temps()
print(f"The daily temperatures are: {daily_temps}")