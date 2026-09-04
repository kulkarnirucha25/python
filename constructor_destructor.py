class rectangle:
    def __init__(self,lenght,breadth):
        self.lenght=lenght
        self.breadth=breadth

    def area(self):
        return self.lenght*self.breadth

    def __del__(self):
     print("constructor destroyed")    

r=rectangle(10,20)
print("area of rectangle is ",r.area())
del r
