from datetime import datetime


class Person:
    number_created = 0

    def __init__(self, fname, lname, gender, birthdate):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.birthdate = birthdate
        Person.number_created += 1

    def full_name(self):
        print(self.fname, self.lname)
        return # why are the returns added at the end of each method
    # def days_until_birthday(self, birthdate):
    #     now = datetime.now()
    #     (t - datetime.datetime(1970, 1, 1)).total_seconds()
    #     day =
    #     year
    #     month
    #     birthdate

    def change_of_name(self, new_name):
        self.lname = new_name
        return


if __name__ == "__main__":
    p1 = Person("Nina", "Jolly", "Female", "04/05/1989")
    print(p1.full_name())
