# define a class
class Employee:
    # define a property
    employee_id = 0
    employee_gender = ""
    employee_name = ""
    employee_yob = 0
    currentYear = 0
    startingYear = 0
# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access property using employee1
employee1.employee_id = 1001
print(f"Employee ID: {employee1.employee_id}")

# access properties using employee2
#employee2.employeeID = 1002
#print(f"Employee ID: {employee2.employeeID}")

employee1.employee_yob= 3456
print(f"Employee Year of Birth: {employee1.employee_yob}")

employee1.employee_name = "Tabitha"
print(f"Employee ID: {employee1.employee_name}")
    
