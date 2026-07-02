from datetime import datetime

class Transaction:
    def __init__(
            self, 
            transaction_type, 
            amount, 
            balance, 
            account_type):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
        self.account_type = account_type
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"""
            ----- RECEIPT -----
            Type: {self.transaction_type}
            Amount: ${self.amount}
            Account: {self.account_type}
            Balance: ${self.balance}
            Date: {self.date}
            -------------------
        """