class Rectangle:
    #initialize the class
    def __init__(self,height = 0, width = 0):
        self.height = height
        self.width = width


    #method to calculate area
    def getArea(self):
        return (self.height * self.width)
    

class Circle:
    #initialize the class
    def __init__(self,radius = 0):
        self.radius = radius

    #method to calculate area
    def getArea(self):
        return (3.14 * self.radius * self.radius)
    

#creating objects of the classes
obj1 = Rectangle(10,20)
obj2 = Circle(7)
print("Area of rectangle:", obj1.getArea())
print("Area of circle:", obj2.getArea())
# The output of the above code will be:
# Area of rectangle: 200
# Area of circle: 153.86
    

