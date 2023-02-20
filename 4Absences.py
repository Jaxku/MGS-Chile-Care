# Define the list to hold the employee data
employees = []

# Read in employee data until a $ symbol is entered
while True:
    data = input("Enter employee name and days absent (or $ to finish): ")
    if data == "$":
        break
    employees.append(data.split())

# Calculate the average number of days absent per year
total_days_absent = sum(int(employee[1]) for employee in employees)
average_days_absent = total_days_absent / len(employees)

# Find the person with the most days absent
most_absent_employee = max(employees, key=lambda employee: int(employee[1]))

# Find the employees who were not absent at all
not_absent_employees = sorted([employee[0] for employee in employees if employee[1] == '0'])

# Find the employees whose period of absence was above the average
above_average_employees = sorted([employee for employee in employees if int(employee[1]) > average_days_absent], key=lambda employee: (-int(employee[1]), employee[0]))

# Print the results
print("Average number of days staff were absent: {:.2f}".format(average_days_absent))
print("Person with most days absent: {} with {} days".format(most_absent_employee[0], most_absent_employee[1]))
print("List of people not absent at all:")
for employee in not_absent_employees:
    print(employee)
print("List of people absent above average:")
for employee in above_average_employees:
    print("{} {}".format(employee[0], employee[1]))
