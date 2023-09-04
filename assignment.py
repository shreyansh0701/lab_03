# Define the Employee Table as a list of dictionaries
employee_table = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000},
]

# Function to print the Employee Table
def print_employee_table(table):
    print("\nEmployee Table:")
    print("{:<12} {:<10} {:<4} {:<15}".format("Employee ID", "Name", "Age", "Salary (PM)"))
    for employee in table:
        print("{:<12} {:<10} {:<4} {:<15}".format(employee["Employee ID"], employee["Name"], employee["Age"], employee["Salary (PM)"]))

# Function to sort the Employee Table by Age
def sort_by_age(table):
    return sorted(table, key=lambda x: x["Age"])

# Function to sort the Employee Table by Name
def sort_by_name(table):
    return sorted(table, key=lambda x: x["Name"])

# Function to sort the Employee Table by Salary
def sort_by_salary(table):
    return sorted(table, key=lambda x: x["Salary (PM)"])

# Main program
while True:
    print("\nChoose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        sorted_table = sort_by_age(employee_table)
    elif choice == "2":
        sorted_table = sort_by_name(employee_table)
    elif choice == "3":
        sorted_table = sort_by_salary(employee_table)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option.")
        continue
    
    print_employee_table(sorted_table)

print("Program terminated.")
