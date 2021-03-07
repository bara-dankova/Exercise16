from person import Person
from employee import Employee
from customer import Customer


p1 = Person("Nina", "Jolly", "Female", [1980, 12, 12])
print(p1.full_name())
p1.change_of_name("Batt")
print(p1.full_name())
# why are there None's after each print


worker_1 = Employee("John", "Doe", "Male", [1985, 12, 12], "marketing", "Loud")

print(worker_1.email)
print(worker_1)
print(worker_1.employee_number)
worker_1.employee_number()
print(worker_1.employee_number)
worker_1.employee_number()
print(worker_1.employee_number)
