from models.transaction import Transaction

class Account:
    def __init__ (self, account_type, account_number, balance):
        self.account_type = account_type
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
            print("Insufficient funds")
            return

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
        if( len(self.transactions) == 0):
            print(f"No transactions found for account {account_number}.")
            return
        
        print(f"Transaction history for account {account_number}:")
        for transaction in self.transactions:
            print(transaction)