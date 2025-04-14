'''A program that does the following:
 a.Write a query to select only the Name and Salary columns.
 b.How would you filter out all employees in the "IT" department?
 c.  Write code to select employees who are older than 30 and find the average salary of employees in each department.
 d.Write code to count the number of employees in each department.
 e.Add a new column Bonus which is 10% of each employee's salary.
 f.Replace all occurrences of "HR" in the Department column with "Human Resources."
 g.Find the employee(s) with the longest tenure (based on JoinDate).
 h.Create a new column SalaryCategory where salaries above 75,000 are categorized as "High" and the rest as "Low."
 i.  Write a program to check if there are any duplicate EmployeeIDs and remove them if found.
 j.Use Pandas to calculate the median Age of all employees.
'''
import pandas as pd
import numpy as np

# Define employee data
employee_data = {
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["John Smith", "Alice Brown", "Bob White", "Emma Green", "Charlie Red"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Age": [30, 28, 35, 40, 25],
    "Salary": [70000, 60000, 80000, 90000, 55000],
    "JoinDate": ["2018-07-15", "2020-03-10", "2016-11-01", "2012-05-25", "2021-06-01"],
    "ExperienceYears": [5, 3, 7, 11, 2]
}

# Create a DataFrame from the employee data
df = pd.DataFrame(employee_data)

# **a. Select Name and Salary columns**
name_and_salary = df[["Name", "Salary"]]  # Select only the Name and Salary columns
print(f"Name and Salary columns:\n{name_and_salary}\n")

# **b. Filter IT department employees**
it_employees = df[df["Department"] == "IT"]  # Filter employees in the IT department
print(f"Employees in the IT department:\n{it_employees}\n")

# **c. Calculate average salary for employees older than 30**
older_than_30 = df[df["Age"] > 30]  # Select employees older than 30
avg_salary_older_than_30 = older_than_30.groupby("Department")["Salary"].mean()  # Calculate average salary for each department
print(f"Average salary of employees older than 30:\n{avg_salary_older_than_30}\n")

# **d. Count employees in each department**
department_counts = df["Department"].value_counts()  # Count employees in each department
print(f"Number of employees in each department:\n{department_counts}\n")

# **e. Calculate bonus for each employee**
df["Bonus"] = df["Salary"] * 0.10  # Calculate 10% bonus for each employee
print(f"Bonus for each employee:\n{df[["Name", "Salary", "Bonus"]]}\n")

# **f. Replace HR with Human Resources in Department column**
df["Department"] = df["Department"].replace("HR", "Human Resources")  # Replace HR with Human Resources
print(f"HR replaced with Human Resources in Department column:\n{df[["Name", "Department"]]}\n")

# **g. Find employees with longest tenure**
df["JoinDate"] = pd.to_datetime(df["JoinDate"])  # Convert JoinDate to datetime format
longest_tenure = df[df["JoinDate"] == df["JoinDate"].min()]  # Find employees with longest tenure
print(f"Employees with longest tenure:\n{longest_tenure[["Name", "JoinDate"]]}\n")

# **h. Create SalaryCategory column**
df["SalaryCategory"] = df["Salary"].apply(lambda x: "High" if x > 75000 else "Low")  # Create SalaryCategory column
print(df[["Name", "Salary", "SalaryCategory"]], "\n")

# **i. Check for duplicate EmployeeIDs**
if df["EmployeeID"].duplicated().any():  # Check for duplicate EmployeeIDs
    df = df.drop_duplicates(subset="EmployeeID")  # Remove duplicate rows
    print("Duplicate ID has been removed")
else:
    print("No Duplicate ID are found.")

print(df[["EmployeeID", "Name"]], "\n")

# **j. Calculate median age**
median_age_value = df["Age"].median()  # Calculate median age
print(f"Median age of all employees is: {median_age_value}\n")