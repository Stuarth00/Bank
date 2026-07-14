from models.bank import Bank
from models.user import User
from models.account import Account
from models.transaction import Transaction

bank = Bank()
luis = bank.create_user("Luis", "luis@gmail.com")
saving = bank.open_account(luis, "saving", 1000)

juan = bank.create_user("Juan", "juan@gmail.com")
checking = bank.open_account(juan, "checking", 500)

print(luis.name)
print(luis.email)
print(luis.accounts[0].account_type)
print(luis.accounts[0].account_number)
print(luis.accounts[0].balance)

print("-----")

bank.transaction(saving.account_number, checking.account_number, 100)
bank.get_history(saving.account_number)


