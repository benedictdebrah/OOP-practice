'''
print('Hello world')

def add(num1 , num2):
    sum = num1 + num2
    return sum
print(add(3,4))

class Employee:
    def __init__(self,Id = None, salary=0, department=None):
        self.Id = Id
        self.salary = salary
        self.department = department

    def tax(self):
        return(self.salary * 0.2)
    
    def salaryPerDay(self):
        return(self.salary / 30)

steve = Employee(32,3333,'Marketing')

#printing them
print('Id' ,steve.Id)
print('salary',steve.salary)
print('department',steve.department)
print('The tax paid  is ',steve.tax())
print('The salary perday is :',steve.salaryPerDay())

'''
'''
class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod #applying class method
    def getTeamName(cls):
        return cls.teamName


print(Player.getTeamName())

'''

'''
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property


Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
print("Salary:", Steve.__salary)  # this will cause an error

'''

#challenge 1

class Task:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z =z
    
    def sqSum(self):
        a = self.x * self.x
        b = self.y * self.y
        c = self.z * self.z
    
        return(a + b + c)
    
obj = Task(4,5,6)
print(obj.sqSum())
