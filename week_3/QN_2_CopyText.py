'''a program to copy the contents of one file to another.'''

# A function to copy the contents of one file to another
def copy_file():
    # Prompting the user to enter the name of the source file
    source = input("Enter the name of source file: ")
    
    # Prompting the user to enter the name of the destination file
    destination = input("Enter the name of destination file: ")

    try:
        # Opening the source file in read mode and store its content
        with open(source, 'r') as source_file:
            content = source_file.read()
            # Printing the content of the source file
            print(content)

        # Opening the destination file in write mode and write the content
        with open(destination, 'w') as destination_file:
            destination_file.write(content)
        # Printing a success message
        print("You have copied the content of the file successfully")

    except FileNotFoundError:
        # Handling the case when the source file does not exist
        print("The file does not exist")

    except Exception as e:
        # Handling any other exceptions and print the error message
        print(f"An error occurred: {e}")

# A loop to allow the user to copy multiple files
while True:
    # Calling the copy_file function
    copy_file()
    # Prompting the user to enter whether they want to copy another file
    cont = input("Do you want to copy another file? (yes/no): ")
    # If the user enters anything other than "yes", breaking the loop
    if cont.lower() != "yes":
        break