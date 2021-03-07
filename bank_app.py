from account import Account
from premium_account import PremiumAccount

# instantiate a bank account object
Lisa = Account("Lisa", 500, 3)

# test bank account - object dot attribute
Lisa.deposit(40)
Lisa.get_balance()
Lisa.withdraw(100)
Lisa.get_balance()
print(Lisa)


# instantiate a premium bank account object
Michelle = PremiumAccount("Michelle", 10000, 3, 0.05)
print(Michelle)

# test over three withdrawals
Michelle.withdraw(500)
print(Michelle)
Michelle.withdraw(500)
print(Michelle)
Michelle.withdraw(500)
print(Michelle)
Michelle.withdraw(500)
print(Michelle)

# test deposit with interest in premium account
Michelle.deposit(1000)
print(Michelle)
