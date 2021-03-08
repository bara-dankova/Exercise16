from person import Person
from employee import Employee
from customer import Customer

# test Person attributes and methods
p1 = Person("Nina", "Jolly", "Female", "12/12/1980")
print(p1.full_name())
p1.change_of_name("Batt")
print(p1.full_name())
# test number of people
print("Number of people created:", Person.number_created)
print("-"*20)
# TODO why are there None's after each print



# test worker attributes
worker_1 = Employee("John", "Doe", "Male", "12/12/1985", "marketing", "Loud")
print(worker_1.email)
print(worker_1)
print(worker_1.employee_number)
print("-"*20)


# test Customer attributes and methods
Anna = Customer("Anna", "Smith", "Female", "09/03/1996", True, False)
print(Anna)
Anna.book_trip()
Anna.book_jab()
Anna.book_trip()
Anna.shop(300)
print(Anna.loyalty_points)

