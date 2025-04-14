'''a program that counts the occurrence of each word in a file'''

document_title = input("Please enter the document name: ")

try: 
    # Accessing the document in text mode
    with open(document_title, "r") as document:  # Opens the document in text mode
        text_data = document.read()
    
    text_data = text_data.lower()  # Transforms the text to lowercase
    phrases = text_data.split()  # Divides the text into phrases
    phrase_frequency = {}  #empty dictionary

    # Examining each phrase
    for phrase in phrases:
        if phrase not in phrase_frequency:  # Checks if the phrase is not already in the dictionary
            phrase_frequency[phrase] = 1  # Adds the phrase with an initial frequency of 1
        else:
            phrase_frequency[phrase] += 1  # Increments the frequency for repeated phrases

    # Display the phrase frequencies
    print("\nPhrases and their frequency:")
     # Each phrase and its frequency iterates through the dictionary
    for phrase, frequency in phrase_frequency.items():  #.items() returns key-value pairs as tuples
        document_phrase = phrase
        frequency_count = frequency
        print(f"{document_phrase}: {frequency_count}")

except FileNotFoundError:
    print("The document was not found.")
except Exception as e:
    print(f"The issue is {e}")