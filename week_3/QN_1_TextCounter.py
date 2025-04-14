'''A program to count the number of lines, words, and characters in a text file.'''

# Open the file in read mode
file = open("program1.txt", 'r')
# Calculate the total number of lines in the file
total_lines = len(file.readlines())
print('Total number of lines in the file:', total_lines)

# Reset the file pointer to the beginning of the file
file.seek(0) 
# Initialize a counter for the total number of words
total_word_count = 0
# Read the entire file content into a string
file_content = file.read() 
# Split the content into individual words
word_list = file_content.split() 
# Iterate over each word in the list
for word in word_list:
  total_word_count += 1
print(f"Total number of words in the file: {total_word_count}")

# Initialize a counter for the total number of characters
total_char_count = 0
# Iterate over each character in the file content
for char in file_content: 
  total_char_count += 1
print(f"Total number of characters in the file: {total_char_count}")
file.close()