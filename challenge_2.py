class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return(self.phy + self.chem + self.bio)

    def Percentage(self):
        return((self.totalObtained() / 300) * 100)
    
obj = Student('ama',23,34,56)
print(obj.Percentage())