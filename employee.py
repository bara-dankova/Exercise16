from person import Person
import random

class Employee(Person):
    def __init__(self, fname, lname, gender, birthdate, sector, company):
        # can we inherit less attributes than superclass has?
        Person.__init__(self, fname, lname, gender, birthdate)
        self.sector = sector
        self.company = company
        # set employee number at instanciation once - can print same number multiple times
        self.employee_number = "Your employee number is: {}".format(random.randint(1, 500))

    #def work_email(self):
     #   self.email = str(self.fname) + "." + str(self.lname) + "@" + str(self.company) + ".co.uk"

    @property #defining email like a method but can access it like an attribute
    def email(self):
        return '{}.{}@{}.co.uk'.format(self.fname, self.lname, self.company)

    def __str__(self):
        return "Employee: ('{}', '{}')".format(self.fname, self.lname)

    # what does this do?
    def __repr__(self):
        return "Employee: ('{}', '{}')".format(self.fname, self.lname)

    # set an employee number - can't run twice (error)
    #def employee_number(self):
    #    self.employee_number = random.randint(1, 500)

    #def __getattr__(self, fname):
    #        return fname + " is here!"

if __name__ == "__main__":
    worker_1 = Employee("John", "Doe", "Male", [1985, 12, 12], "marketing", "Loud")
    print(worker_1.email)


