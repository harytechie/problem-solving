import matplotlib.pyplot as plt

labels = ['Hary', 'Rahul', 'ravi', 'gokul']
sizes = [15, 30, 45, 10]
colors = ['skyblue', 'orange', 'green', 'black']
plt.pie(sizes, labels=labels, colors=colors, autopct='%2.0f%%')
plt.title("Simple Pie Chart")
plt.show()
