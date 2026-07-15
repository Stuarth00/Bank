from models.exceptions import InsufficientFundsError
from models.transaction import Transaction

class Account:
    account_type = "generic"
    def __init__ (self, account_number, balance):

        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount, from_account_number=None, to_account_number=None):
        self.balance += amount

        transaction = Transaction(
            "deposit", 
            from_account_number,
            to_account_number,
            amount, 
            self.balance,
            self.account_type
        )
        self.transactions.append(transaction)
        return transaction

    def withdraw(self, amount, from_account_number=None, to_account_number=None):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )

        self.balance -= amount

        transaction = Transaction(
            "withdraw", 
            from_account_number,
            to_account_number,
            amount, 
            self.balance,
            self.account_type
        )
        self.transactions.append(transaction)
        return transaction
    
    def show_history(self, account_number): 
        if not self.transactions: 
            print(f"No transactions found for account {account_number}.")
            return
        
        print(f"Transaction history for account {account_number}:")
        for transaction in self.transactions:
            print(transaction)

class SavingAccount(Account):
    account_type = "saving"
    WITHDRAWAL_LIMIT = 6;

    def withdraw(self, amount, from_account_number=None, to_account_number=None):
        if len([t for t in self.transactions if t.transaction_type == "withdraw"]) >= self.WITHDRAWAL_LIMIT:
            raise Exception(f"Withdrawal limit of {self.WITHDRAWAL_LIMIT} reached for account {self.account_number}.")
        return super().withdraw(amount, from_account_number, to_account_number)

class CheckingAccount(Account):
    account_type = "checking"
    OVERDRAFT_LIMIT = 500; 

    def withdraw(self, amount, from_account_number=None, to_account_number=None):
        if amount > self.balance + self.OVERDRAFT_LIMIT:
            raise InsufficientFundsError("Exceeds overdraft limit.")
        self.balance -= amount
        transaction = Transaction(
            "withdraw", 
            from_account_number,
            to_account_number,
            amount, 
            self.balance,
            self.account_type
        )
        self.transactions.append(transaction)
        return transaction

class CreditAccount(Account):
    account_type = "credit"

    def __init__(self, account_number, credit_limit):
        super().__init__(account_number, 0)  
        self.credit_limit = credit_limit

    def withdraw(self, amount, from_account_number=None, to_account_number=None):
        if amount > self.credit_limit - self.balance:
            raise InsufficientFundsError("Exceeds credit limit.")
        self.balance += amount
        transaction = Transaction(
            "withdraw", 
            from_account_number,
            to_account_number,
            amount, 
            self.balance,
            self.account_type
        )
        self.transactions.append(transaction)
        return transaction
