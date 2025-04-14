''' A program to find and replace a specific word in a file with another word.'''

# Getting the user input
file_name = input('Enter the name of your file: ')
old_word = input('Enter the word that should be replaced: ')
new_word = input('Enter the new word: ')

# Checking if the file exists
try:
    with open(file_name, 'r') as file:
        content = file.read()

        # Checkinf if the file is not empty
        if not content:
            print("The file is empty.")
            exit()

        # Checking if the old word is found in the file
        if old_word not in content:
            print("The word '{}' is not found in the file.".format(old_word))
            exit()

        # Checking if the new word is different from the old word
        if old_word == new_word:
            print("The new word is the same as the old word.")
            exit()

        # Replacing the old word with the new word
        replaced_content = content.replace(old_word, new_word)

        # Writing the modified content back to the file
        with open(file_name, 'w') as file:
            file.write(replaced_content)
            print("The word replaced successfully.")

except FileNotFoundError:
    print("The file does not exist.")

except Exception as e:
    print("An error occurred: {}".format(e))