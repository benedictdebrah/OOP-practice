class Student:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self,Rollnumber):
        self.__Rollnumber = Rollnumber
        

    def getRollNumber(self):
        return self.__Rollnumber
    
demo1 = Student()
demo1.setName("Alex")
print("Name:", demo1.getName())
demo1.setRollNumber(3789)
print("Roll Number:", demo1.getRollNumber())