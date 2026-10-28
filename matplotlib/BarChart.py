import matplotlib.pyplot as plt

names = ["A", "B", "C", "D", "E"]
marks = [35, 15, 8, 10, 12]
plt.bar(names, marks)
plt.title("Student Marks")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.show()
