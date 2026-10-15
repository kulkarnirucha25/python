import numpy as np

x = int(input("Enter the number of blocks: "))
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

arr = []

for i in range(x):
    block = []

    for j in range(r):
        row = []

        for k in range(c):
            n = int(input("Enter element: "))
            row.append(n)

        block.append(row)

    arr.append(block)

a = np.array(arr)

print("The 3D array is:")
print(a)