from account import Account
from premium_account import PremiumAccount
from loan_account import LoanAccount

# instantiate a bank account object
Lisa = Account("Lisa", 500, 3)

# test bank account - object dot attribute
Lisa.deposit(40)
Lisa.get_balance()
Lisa.withdraw(100)
Lisa.get_balance()
print(Lisa)
Lisa.get_account_number()
print("-"*20)

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
print("-"*20)

# tested loan account methods
loan_1 = LoanAccount("Bara", -10000, 3, 0.25, "good")

#print(loan_1.get_total_amount())
print(loan_1.credit_rating)
loan_1.get_credit_rating()
print(loan_1.make_payment(500))
loan_1.get_balance()
loan_1.payment_schedule()