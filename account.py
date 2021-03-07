#account file
class Account:
    numCreated = 0
    # constructor gets called automatically
    def __init__(self, name, initial, withdrawal_fee):
        self.name = name
        self._balance = initial
        self.withdrawal_fee = withdrawal_fee
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
