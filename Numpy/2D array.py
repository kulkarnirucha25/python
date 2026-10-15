import numpy as np

r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of columns:"))
arr = []

for i in range(r):
    row = []
    for j in range(c):
        x = int(input("Enter element:"))
        row.append(x)
    arr.append(row)

a = np.array(arr)
print("The 2D array is :")
print(a)