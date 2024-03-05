class Com:
    def __init__(self, real = 0, imag = 0) :
        self.real = real
        self.imag = imag

    
    def __add__(self, num):
        temp = Com(self.real + num.real, self.imag + num.imag)
        return temp
    
    def __sub__(self, num):
        temp = Com(self.real - num.real, self.imag - num.imag)
        return temp
    
#method to make calculations
obj = Com(3, 7)
obj2 = Com(2, 5)
obj3 = obj + obj2
obj4 = obj - obj2
print("Real of obj3:", obj3.real)
print("Imag of obj3:", obj3.imag)
print("Real of obj4:", obj4.real)
print("Imag of obj4:", obj4.imag) 
# The output of the above code will be: 

