from models.bank import Bank
from models.user import User
from models.account import Account
from models.transaction import Transaction

bank = Bank()
luis = User("Luis", "luis@gmail.com")
bank.add_user(luis)

checking = Account('Checking', 1000)
luis.add_account(checking)

print(bank.users[0].name)
print(bank.users[0].email)
print(bank.users[0].accounts[0].account_type)
print(bank.users[0].accounts[0].balance)

checking.deposit(500) 

# checking.withdraw(1990)
checking.withdraw(800)

# transaction = Transaction()
# print(transaction[0])