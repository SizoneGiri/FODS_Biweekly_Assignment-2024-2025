'''A program that has a function called add_daily_temp that is given a (possibly empty) dictionary meant to hold the average daily temperature
 for each day of the week, a temperature value, and the day of the week for the recorded temperature. 
 The function then adds the temperature to the dictionary only if it does not already contain a temperature for that day.
 The function then returns the resulting dictionary, whether it is updated or not.'''

#Function to add the daily temperature to the dictionary
def add_daily_temp(temp_dic, temperature, Day):
    if Day not in temp_dic:
        temp_dic[Day] = [temperature] # Add temperature to the list for the day
    return temp_dic #returns the updated dictionary

#Dictionary to hold the average daily temperature for each day of the week
temperature_weekly = {'Sunday' : 25,'Tuesday':281, 'Thursday':30 }

#here we pass the dictionary, temperature and day to the function
temperature_weekly = add_daily_temp(temperature_weekly,31,'Sunday') 
temperature_weekly = add_daily_temp(temperature_weekly,40,'Friday')
temperature_weekly = add_daily_temp(temperature_weekly,35,'Wednesday')

print(temperature_weekly) # prints the updated dictionary
