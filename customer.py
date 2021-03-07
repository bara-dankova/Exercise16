from person import Person


class Customer(Person):
    def __init__(self, fname, lname, gender, birthdate, staff):
        Person.__init__(self, fname, lname, gender, birthdate)
        self.staff = staff
        self.loyalty_points = 0

    def shop(self, price):
        self.loyalty_points += price/10
        if self.staff == True:
            self.loyalty_points += price/20

    def __str__(self):
        return "Customer: \nName: {}, Surname: {}, Points: {}".format(self.fname, self.lname, self.loyalty_points)

    def __repr__(self):
        return f"fname={self.fname}, lname={self.lname}, gender={self.gender}, birthdate={self.birthdate}"


if __name__ == "__main__":
    Anna = Customer("Anna", "Smith", "Female", [1990, 11, 2], True)
    print(Anna.full_name())
    print(Anna.loyalty_points)
    Anna.shop(250)
    print(Anna.loyalty_points)
    print(Anna.gender)
    print(Anna)
