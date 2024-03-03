class Account: #parent class

    #initializing the class
    def __init__(self,title = None, balance = 0):
        self.title = title
        self.balance = balance
    
    #method to view balance
    def getBalance(self):
        return self.balance
    
    #method to deposist money
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    #method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance'
        else:
            self.balance -= amount
            return self.balance
        
class SavingsAccount(Account): #child class
    def __init__(self, title = None, balance = 0, interestRate = 0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    #method to calculate interest
    def interestAmount(self):
        return (self.interestRate * self.balance)/100
    

    
obj1 = SavingsAccount("Steve", 5000, 10)
print("Initial Balance:", obj1.getBalance())
obj1.withdraw(1000)
print("Balance after withdrawal:", obj1.getBalance())
obj1.deposit(500)
print("Balance after deposit:", obj1.getBalance())
print("Interest on current balance:", obj1.interestAmount())
