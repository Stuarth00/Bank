import random
from models.user import User
from models.account import Account, CheckingAccount, CreditAccount, SavingAccount

class Bank:
    ACCOUNT_TYPES = {
        "saving": SavingAccount,
        "checking": CheckingAccount, 
        "credit": CreditAccount
    }
 
    def __init__ (self):
        self.users = []
        self.accounts = {}

    def create_user(self, name, email):
        user = User(name, email)
        self.users.append(user)
        return user
    
    def open_account(self, user, account_type, balance):
        account_class = self.ACCOUNT_TYPES.get(account_type.lower())
        if account_class is None:
            raise ValueError(f"Invalid account type: {account_type}. Valid types are: {', '.join(self.ACCOUNT_TYPES.keys())}")

        account_number = self.gen_account_number()
        account = account_class(account_number, balance)

        self.accounts[account_number] = account
        user.add_account(account)
        return account
    
    def gen_account_number(self, digits = 8):
        first_digit = random.choice('123456789')  # First digit cannot be zero
        other_digits = ''.join(random.choices('0123456789', k=digits - 1))
        account_number = first_digit + other_digits
        
        while account_number in self.accounts:
            first_digit = random.choice('123456789')  # First digit cannot be zero
            other_digits = ''.join(random.choices('0123456789', k=digits - 1))
            account_number = first_digit + other_digits
        return account_number
    
    def get_account(self, account_number):
        print(f"Account found: {account_number}, Balance: ${self.accounts[account_number].balance}, Type: {self.accounts[account_number].account_type}, and owner: {[user.name for user in self.users if self.accounts[account_number] in user.accounts]}")
        return self.accounts.get(account_number)
    
    def get_user(self, email):
        for user in self.users:
            if user.email == email:
                print(f"User found: {user.name}, Email: {user.email}, and Accounts: {[account.account_number for account in user.accounts]}")
                return user
        return None

    def transaction(self, from_account_number, to_account_number, amount):
        source = self.accounts.get(from_account_number)
        destination = self.accounts.get(to_account_number)

        if source is None or destination is None:
            print("One of the accounts does not exist.")
            return
        
        withdraw_receipt = source.withdraw(amount, from_account_number, to_account_number)
        deposit_receipt = destination.deposit(amount, from_account_number, to_account_number)

        print(withdraw_receipt)
        print(deposit_receipt)

    def get_history(self, account_number):
        account = self.accounts.get(account_number)

        if account is None: 
            print("Account does not exist.")
            return

        account.show_history(account_number)