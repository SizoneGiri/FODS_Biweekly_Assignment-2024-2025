''' A program to read a CSV file and display its contents in a tabular format'''

import csv

user_input = input('Please enter the CSV file name: ')

try:
  with open(user_input,'r')as data_file: #opens the file for reading
    data_reader = csv.reader(data_file)  #reads the file content line by line
    print ("\nCSV File Contents:")

    for data_line in data_reader:
         #formatting for better readability
         print('\t'.join(data_line)) #lines are printed separated by tabs 

except FileNotFoundError:
   print("File not found in the system")

except Exception as error_message:
   print (f"An error occurred: {error_message}")