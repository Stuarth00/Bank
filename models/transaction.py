from datetime import datetime

class Transaction:
    def __init__(
            self, 
            transaction_type, 
            from_account_number,
            to_account_number,
            amount, 
            balance, 
            account_type):
        self.transaction_type = transaction_type
        self.from_account_number = from_account_number
        self.to_account_number = to_account_number
        self.amount = amount
        self.balance = balance
        self.account_type = account_type
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"""
            ----- RECEIPT -----
            Type: {self.transaction_type}
            From Account: {self.from_account_number}
            To Account: {self.to_account_number}
            Amount: ${self.amount}
            Account: {self.account_type}
            Balance: ${self.balance}
            Date: {self.date}
            -------------------
        """