class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num1 + self.num2)
    
    def subtract(self):
        return (self.num1 - self.num2)
    
    def multiply(self):
        return (self.num1 *  self.num2)
    
    def divide(self):
        return (self.num1 / self.num2)
    
obj = Calculator(10,40)
print('The addition of the two numbers is',obj.add())
print('The subtraction of the two numbers is',obj.subtract())
print('The multiplication of the two numbers is',obj.multiply())
print('The division of the two numbers is',obj.divide())
