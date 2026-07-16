from models.exceptions import InsufficientFundsError, InvalidAmountError
from models.transaction import Transaction

class Account:
    account_type = "generic"
    def __init__ (self, account_number, balance):

        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount, from_account_number=None, to_account_number=None):
        if amount <= 0:
            raise InvalidAmountError(f"Invalid deposit amount: {amount}. Amount must be greater than zero.") 
        
        self.balance += amount
        return self._record_transaction("deposit", amount, from_account_number, to_account_number)

    def withdraw(self, amount, from_account_number=None, to_account_number=None):
        if amount <= 0:
            raise InvalidAmountError(f"Invalid withdrawal amount: {amount}. Amount must be greater than zero.") 
        
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )

        self.balance -= amount
        self._record_transaction("withdraw", amount, from_account_number, to_account_number)
    
    def show_history(self): 
        if not self.transactions: 
            print(f"No transactions found for account {self.account_number}.")
            return
        
        print(f"Transaction history for account {self.account_number}:")
        for transaction in self.transactions:
            print(transaction)

    def _record_transaction(self, transaction_type, amount, from_account_number, to_account_number):
        transaction = Transaction(
            transaction_type, 
            from_account_number, 
            to_account_number, 
            amount, 
            self.balance, 
            self.account_type
        )
        self.transactions.append(transaction)
        return transaction

class SavingAccount(Account):
    account_type = "saving"
    WITHDRAWAL_LIMIT = 6;

    def withdraw(self, amount, from_account_number=None, to_account_number=None):
        if len([t for t in self.transactions if t.transaction_type == "withdraw"]) >= self.WITHDRAWAL_LIMIT:
            raise Exception(f"Withdrawal limit of {self.WITHDRAWAL_LIMIT} reached for account {self.account_number}.")
        return self._record_transaction("withdraw", amount, from_account_number, to_account_number)

class CheckingAccount(Account):
    account_type = "checking"
    OVERDRAFT_LIMIT = 500; 

    def withdraw(self, amount, from_account_number=None, to_account_number=None):
        if amount > self.balance + self.OVERDRAFT_LIMIT:
            raise InsufficientFundsError("Exceeds overdraft limit.")
        self.balance -= amount
        return self._record_transaction("withdraw", amount, from_account_number, to_account_number)

class CreditAccount(Account):
    account_type = "credit"

    def __init__(self, account_number, credit_limit):
        super().__init__(account_number, 0)  
        self.credit_limit = credit_limit

    def withdraw(self, amount, from_account_number=None, to_account_number=None):
        if amount > self.credit_limit - self.balance:
            raise InsufficientFundsError("Exceeds credit limit.")
        self.balance += amount
        return self._record_transaction("withdraw", amount, from_account_number, to_account_number)
