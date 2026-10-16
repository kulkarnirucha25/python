import pandas as pd

n = int(input("Enter number of elements: "))

data = []

for i in range(n):
    x = int(input("Enter element: "))
    data.append(x)

s = pd.Series(data)

print("Pandas Series:")
print(s)