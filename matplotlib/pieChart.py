import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
sizes = [35, 15, 8, 10, 12]
plt.pie(sizes, labels=labels)
plt.title("Student Marks")
plt.show()