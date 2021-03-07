from person import Person
from employee import Employee
from customer import Customer


p1 = Person("Nina", "Jolly", "Female", [1980, 12, 12])
print(p1.full_name())
p1.change_of_name("Batt")
print(p1.full_name())
# TODO why are there None's after each print


worker_1 = Employee("John", "Doe", "Male", [1985, 12, 12], "marketing", "Loud")

# test worker attributes
print(worker_1.email)
print(worker_1)
print(worker_1.employee_number)

# test number of people
print(Person.number_created)
