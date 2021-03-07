from person import Person
import random

class Employee(Person):
    def __init__(self, fname, lname, gender, sector, company):
        super().__init__(self, fname, lname, gender)
        self.sector = sector
        self.company = company

    def work_email(self):
        self.email = str(self.fname) + "." + str(self.lname) + "@" + str(self.company) + ".co.uk"

    #def employee_number(self):
        #self.employee_number = random.randint(1, 500)


worker_1 = Employee("John", "Doe", "Male", "marketing", "Loud")

worker_1.work_email()
print(worker_1.email)
