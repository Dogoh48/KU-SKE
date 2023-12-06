class AccountDB:
    def __init__(self):
        self.account_database = []

    def insert(self, account):
        index = self.search_index(account.number)
        if index == -1:
            self.account_database.append(account)
        else:
            print(account, "Duplicated account; nothing to be insert")

    def delete(self, number):
        for i in range(len(self.account_database)):
            if self.account_database[i].number == number:
                del self.account_database[i]

    def search_index(self, number):
        for i in range(len(self.account_database)):
            if self.account_database[i].number == number:
                return i
        return -1
    
    def search_public(self, number):
        for account in self.account_database:
            if account.number == number:
                return account
        return None
    
    def __str__(self):
        s = ''
        for account in self.account_database:
            s += str(account) + ", "
        return s
            
class Account:
    def __init__(self, num, type, name, init_balance):
        self.number = num
        self.type = type
        self.name = name
        self.balance = init_balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount

    def __str__(self):
        return '{' + str(self.number) + ',' + str(self.type) + ',' + str(self.name) + ',' + str(self.balance) + '}'
    


account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)
account4 = Account("0004", "saving", "David Wood", 4000)
account5 = Account("0004", "saving", "David Wood", 4000)
my_account_DB = AccountDB()
my_account_DB.insert(account1)
my_account_DB.insert(account2)
my_account_DB.insert(account3)
my_account_DB.insert(account4)
my_account_DB.insert(account5)
print(my_account_DB)
my_account_DB.search_public("0003").deposit(50)
print(my_account_DB)
my_account_DB.search_public("0003").withdraw(100)
print(my_account_DB)
my_account_DB.delete('0004')
print(my_account_DB)