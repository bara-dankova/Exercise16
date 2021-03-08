from person import Person
import random
import datetime


class Employee(Person):
    def __init__(self, fname, lname, gender, birthdate, sector, company):
        #TODO can we inherit less attributes than superclass has?
        Person.__init__(self, fname, lname, gender, birthdate)
        self.sector = sector
        self.company = company
        self.hours = 0
        # set employee number at instantiation once - can print same number multiple times
        self.employee_number = "Your employee number is: {}".format(random.randint(1, 500))

    def work_hours(self, hours):
        self.hours += hours

    def total_hours(self):
        print(self.hours)

    @property # defining email like a method but can access it like an attribute
    def email(self):
        return '{}.{}@{}.co.uk'.format(self.fname, self.lname, self.company)

    def __str__(self):
        return "Employee: ('{}', '{}')".format(self.fname, self.lname)

    #TODO what does the __repr__ do?
    def __repr__(self):
        return "Employee: ('{}', '{}')".format(self.fname, self.lname)

    #TODO we are concerned the employee number can't be run twice as a method (error)

    # def employee_number(self):
    #    self.employee_number = random.randint(1, 500)

    def __getattr__(self, fname):
        return fname + " is here!"


if __name__ == "__main__":
    worker_1 = Employee("John", "Doe", "Male", (datetime.datetime(1985, 12, 12)), "marketing", "Loud")
    print(worker_1.email)
    print(worker_1.total_hours())
    worker_1.work_hours(8)
    worker_1.work_hours(4)
    print(worker_1.total_hours())

