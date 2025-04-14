'''A program to implement a basic library book management with the functionalities such as 
to issue the book, return the book and search the book. 
The program must have:
# Use the concept of OOP to create the necessary classes on your own and implement the concept of other OOP features. 
# For the storage of book details, use the file handling along with the exception handling. '''


# Class to Represent Individual Book Objects

class Publication:
    def __init__(self, catalog_number, publication_title, publication_author):
        self.catalog_number = catalog_number  # Unique Identifier for Publications
        self.publication_title = publication_title  # Title of the Publication
        self.publication_author = publication_author  # Author of the Publication

class Catalog:
    def __init__(self):
        self.publications = []  # Empty List to Store Publication Objects
        self.load_publication_data()  # Load Publication Data from File

    def load_publication_data(self):
        try:
            with open("publications.txt", "r") as file:
                for line in file:
                    catalog_number, publication_title, publication_author = line.strip().split(",")  # Split Line into Catalog Number, Title, and Author
                    self.publications.append(Publication(catalog_number, publication_title, publication_author))  # Add Publication to List
        except FileNotFoundError:
            print("The file does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_publication_data(self):
        with open("publications.txt", "w+") as file:
            for publication in self.publications:
                file.write(f"{publication.catalog_number}, {publication.publication_title}, {publication.publication_author}\n")

    def display_publications(self):
        try:
            if self.publications:
                print("Publications in the Catalog")

                for publication in self.publications:
                    print(f"Catalog Number: {publication.catalog_number}, Title: {publication.publication_title}, Author: {publication.publication_author}")
        except Exception:
            print("No publications available in the catalog.")

    def check_out_publication(self, catalog_number):
        try:
            for publication in self.publications:
                if publication.catalog_number == catalog_number:
                    self.publications.remove(publication)
                    print(f"The publication {publication.publication_title} ({publication.catalog_number}) has been checked out.")
                    self.save_publication_data()
                    return
        except Exception:
            print("Publication not found.")

    def return_publication(self, catalog_number, publication_title, publication_author):
        self.publications.append(Publication(catalog_number, publication_title, publication_author))
        print(f"The publication {publication_title} ({catalog_number}) has been returned.")
        self.save_publication_data()

    def search_publication(self, publication_title):
        for publication in self.publications:
            if publication.publication_title.lower() in publication.publication_title.lower():
                print(f"{publication.publication_title}, {publication.catalog_number} has been found.")
                return
        print("Publication not found.")

def main():
    catalog = Catalog()

    while True:
        print("\n--- Catalog Menu: ---\n")
        print("1. Display Publications")
        print("2. Check Out Publication")
        print("3. Return Publication")
        print("4. Search Publication")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            catalog.display_publications()
        elif choice == "2":
            catalog_number = input("Enter the Catalog Number to check out: ")
            catalog.check_out_publication(catalog_number)
        elif choice == "3":
            catalog_number = input("Enter the Catalog Number to return: ")
            publication_title = input("Enter the Title of the publication: ")
            publication_author = input("Enter the Author of the publication: ")
            catalog.return_publication(catalog_number, publication_title, publication_author)
        elif choice == "4":
            publication_title = input("Enter the Title of the publication to search: ")
            catalog.search_publication(publication_title)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()