'''A program with a function called word_intersection that prompts the user for two English words, 
  and displays which letters the two words have in common.
'''
def word_intersection():
  first_word= input("Enter the first word: ").lower() #lower is used to make case-insensitive
  second_word= input("Enter the second word: ").lower()

  matching_chars=""# initialize empty string to store matches
  for char in first_word:
    #Identifying unique characters in both words
    if char in second_word and char not in matching_chars:
      matching_chars += char

  return matching_chars

shared_chars = word_intersection()
print(f"The words have the following characters in common: {shared_chars}")