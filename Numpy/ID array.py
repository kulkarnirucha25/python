import numpy as np

n = int(input("Enter the size of the array:"))
arr = []

for i in range(n):
    x = int(input("Enter element"))
    arr.append(x)
    a = np.array(arr)

print("The array is :", a)
