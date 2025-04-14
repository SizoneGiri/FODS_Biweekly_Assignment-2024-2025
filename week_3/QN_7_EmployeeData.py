'''A program to implement a class called employee with attributes such as 
 empid, name, address, contact_number, spouse name, number_of_child, salary.
 and do the following:
 Instantiate this class to input the values for multiple employees and write it in a file “employees.csv”. 
 Allow the user of your program to see the list of employees and their details as well. 
 Try to use the concept of try/except too in the program. '''

import csv

class Employee:
    # initializing employee attributes
    def __init__(self, empid, name, address, contact_number, spouse_name, child_count, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.child_count = child_count
        self.salary = salary

def collect_staff_info():  # returns the instance of employee
    try:
        staff_id = int(input("Enter the Staff ID: "))
        staff_name = input("Enter the Staff Name: ")
        staff_address = input("Enter the Staff Address: ")
        staff_contact = int(input("Enter the Staff Contact Number: "))
        staff_spouse = input("Enter the Staff Spouse Name: ")
        staff_children = int(input("Enter the Number of Staff Children: "))
        staff_salary = float(input("Enter the Staff Salary: "))
        return Employee(staff_id, staff_name, staff_address, staff_contact, staff_spouse, staff_children, staff_salary)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def export_staff_to_csv(staff_members, filename="staff_members.csv"):  # writes the list of staff to csv file
    try:
        with open(filename, 'w', newline='') as file:  # open file in write mode
            writer = csv.writer(file)
            # writing the header row to the file
            writer.writerow(["Staff ID", "Staff Name", "Staff Address", "Staff Contact", "Staff Spouse", "Number of Staff Children", "Staff Salary"])
            for staff in staff_members:
                writer.writerow([staff.empid, staff.name, staff.address, staff.contact_number, staff.spouse_name, staff.child_count, staff.salary])
        print("Staff details exported successfully.")
    except Exception as e:
        print(f"A problem occurred: {e}")

def display_staff_members(staff_members):
    if not staff_members:
        print("There is no staff data to display.")
    else:
        for staff in staff_members:  # iterate over the list and displays the details
            print(f"Staff ID: {staff.empid}, Name: {staff.name}, Address: {staff.address}, "
                  f"Contact: {staff.contact_number}, Spouse: {staff.spouse_name}, Children: {staff.child_count}, Salary: {staff.salary}")

def main_program():
    staff_members = []  # initializing empty list
    while True:
        print("\n--- Staff Details ---\n")
        print("1. Add a staff member")
        print("2. Display Staff Details")
        print("3. Export details to the CSV")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            staff = collect_staff_info()
            if staff:  # adds staff if there's no error
                staff_members.append(staff)
        elif choice == 2:
            display_staff_members(staff_members)
        elif choice == 3:
            export_staff_to_csv(staff_members)
        elif choice == 4:
            print("You are exiting the program...")
            break
        else:
            print("Invalid choice. Please choose a valid number (1-4).")

if __name__ == '__main__':
    main_program()  # main function is executed when all the data are valid