# single inheritance
# class square:
#     def __init__(self,side):
#         self.side = side

# class area(square):
#     def calculatearea(self):
#         return self.side*self.side

# a = area(4)
# print ('area of square is:',a.calculatearea())

# multiple inheritance
# class variable:
#     def __init__(self,lenght,breadth):
#         self.lenght=lenght
#         self.breadth=breadth

# class rectangle(variable):
#     def perimeter(self):
#         return 2*(self.lenght+self.breadth)

# class square(variable):
#     def perimeter(self):
#         return 4*self.lenght

# r=rectangle (20,5)
# s=square(10,10)
# print("perimeter of rectangle is ",r.perimeter())
# print("perimeter of square is ",s.perimeter())

# multivel inheritance
# class maths:
#     def __init__(self,no1,no2):
#         self.no1=no1
#         self.no2=no2

#     def add(self):
#         return self.no1 + self.no2

# class science(maths):
#     def sub(self):
#         return self.no1 - self.no2

# class computer(science):
#     def mul(self):
#         return self.no1 * self.no2

# c=computer(10,5)
# print("addition is ",c.add())
# print("subtraction is ",c.sub())
# print("multiplication is ",c.mul())

# hirearchical inheritance
# class bill:
#     def __init__(self,price,quantity):
#         self.price=price
#         self.quantity=quantity

#     def total(self):
#         return self.price*self.quantity

# class item1(bill):
#     def __init__(self,price,quantity):
#        super().__init__(price,quantity)

# class item2(bill):
#     def __init__(self,price,quantity):
#       super().__init__(price,quantity)

# item1=item1(10,5)
# item2=item2(20,10)
# print("total of item1 is ",item1.total())
# print("total of item2 is ",item2.total())

# hybrid inheritance
# class intrest:
#     def __init__(self,amount,rate,time):
#         self.amount=amount
#         self.rate=rate
#         self.time=time

# class simple(intrest):
#     def simpleintrest(self):
#         return (self.amount*self.rate*self.time)/100

# class compound(intrest):
#     def compoundintrest(self):
#         return self.amount*(1+self.rate/100)**self.time

# class total(simple,compound):
#     def totalintrest(self):
#         return self.simpleintrest() + self.compoundintrest()

# t=total(1000,5,2)
# print("simple intrest is ",t.simpleintrest())
# print("compound intrest is ",t.compoundintrest())
# print("total intrest is ",t.totalintrest())
