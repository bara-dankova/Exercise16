from account import Account
from premium_account import PremiumAccount
# instantiate a bank account object
Lisa = Account("Lisa", 500, 3)
# object dot attribute
Lisa.deposit(40)
Lisa.get_balance()
Lisa.withdraw(100)
Lisa.get_balance()
print(Lisa)

Michelle = PremiumAccount("Michelle", 10000, 3, 0.05)
print(Michelle)
Michelle.withdraw(500)
print(Michelle)
Michelle.withdraw(500)
print(Michelle)
Michelle.withdraw(500)
print(Michelle)
Michelle.withdraw(500)
print(Michelle)
Michelle.deposit(1000)
print(Michelle)
