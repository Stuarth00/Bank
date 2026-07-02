from models.transaction import Transaction

class Account:
    def __init__ (self, account_type, balance):
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount

        transaction = Transaction(
            "deposit", 
            amount, 
            self.balance,
            self.account_type
        )
        self.transactions.append(transaction)
        return transaction

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return

        self.balance -= amount

        transaction = Transaction(
            "withdraw", 
            amount, 
            self.balance,
            self.account_type
        )
        self.transactions.append(transaction)
        return transaction