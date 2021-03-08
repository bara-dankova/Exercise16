import random

class Account:
    numCreated = 0
    # constructor gets called automatically

    def __init__(self, name, initial, withdrawal_fee):
        self.name = name
        self._balance = initial
        self.withdrawal_fee = withdrawal_fee
        self._sortcode = "21 21 21"
        self._account_number = random.randint(10000000, 99999999)

    def get_account_number(self):
        print("Your details are as follows:\nSort Code: {} Bank Account Number: {}".format(self._sortcode, self._account_number))

    def __str__(self):
        return "{}'s bank balance is {:.2f}".format(self.name, self._balance)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
        self._balance -= self.withdrawal_fee

    def get_balance(self):
        print(self._balance)


if __name__ == "__main__":
    Lisa = Account("Lisa", 500, 3)
    Lisa.withdraw(100)
    print(Lisa)
    Lisa.get_account_number()