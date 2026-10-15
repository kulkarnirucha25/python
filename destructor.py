# class Student:
#     def __del__(self):
#         print("Destructor called")

# s = Student()
# del s

# class Student:
#     def __init__(self):
#         print("Object created")

#     def __del__(self):
#         print("Object destroyed")

# s = Student()
# del s

# class Student:
#     def __init__(self, name):
#         self.name = name
#         print("Student created:", self.name)

#     def __del__(self):
#         print("Student object destroyed")

# s = Student("Rucha")
# del s

# class Demo:
#     def __init__(self, name):
#         self.name = name
#         print("Created:", self.name)

#     def __del__(self):
#         print("Destroyed:", self.name)

# a = Demo("Object A")
# b = Demo("Object B")

# del a
# del b

# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#         print("Car:", self.brand)

#     def __del__(self):
#         print("Car object deleted")

# c = Car("Toyota")
# del c