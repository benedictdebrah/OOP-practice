class Account:
    def __init__(self,title=None, balance=0):
        self.title = title
        self.__balance = balance

    def getBalance(self):
        super().__init__(self.title, self.__balance)
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance