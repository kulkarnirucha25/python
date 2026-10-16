import matplotlib.pyplot as plt

marks = [45, 50, 60, 65, 70, 70, 80, 85, 90]

plt.hist(marks, bins=5, edgecolor="black")

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()