class Rectangle:
    def __init__(self,length, width) :
        self.__length = length
        self.__width = width

    def Area(self):
        area = self.__length * self.__width
        return area



    def Perimeter(self):
        peri = (2*self.__width) + (2*self.__length)
        return peri
    
calculate = Rectangle(4,5)
print('The area of the rectangle is :',calculate.Area())
print('The perimeter of the rectangle is :',calculate.Perimeter())