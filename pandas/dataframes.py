import pandas as pd

data = {
    "Name": ["Siddhi", "Rucha", "Samruddhi"],
    "Age": [20, 21, 20],
    "Marks": [85, 78, 92]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)