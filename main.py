from models.bank import Bank
from models.user import User
from models.account import Account
from models.transaction import Transaction

bank = Bank()
luis = bank.create_user("Luis", "luis@gmail.com")
credit = bank.open_account(luis, "credit", credit_limit=2000)
saving = bank.open_account(luis, "saving", balance=5000)

juan = bank.create_user("Juan", "juan@gmail.com")
checking = bank.open_account(juan, "checking", balance=1000)

print(luis.name)
print(luis.email)
print(luis.accounts[0].account_type)
print(luis.accounts[0].account_number)
print(luis.accounts[0].credit_limit)

print("-----")

bank.get_account(credit.account_number)
bank.get_account(saving.account_number)

bank.transaction(checking.account_number, saving.account_number, 1000)
bank.get_history(credit.account_number)

# bank.close_account(saving.account_number)
bank.close_user("juan@gmail.com")