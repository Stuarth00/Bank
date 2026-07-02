class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []
        pass

    def add_account(self, account):
        self.accounts.append(account)
                    