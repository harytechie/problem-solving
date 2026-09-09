
# Chart Type              Matplotlib Function
# -------------------------------------------
# Line Chart              - plt.plot()
# Bar Chart (Vertical)    -plt.bar()
# Bar Chart (Horizontal)  -plt.barh()
# Scatter Plot            -plt.scatter()
# Histogram               -plt.hist()
# Pie Chart               -plt.pie()
# Box Plot                -plt.boxplot()
# Violin Plot             -plt.violinplot()
# Area Chart              -plt.fill_between()
# Heatmap                 -plt.imshow() / plt.pcolormesh()




import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 9, 30]

plt.plot(x, y, marker='o', color='blue')

plt.title("My First Matplotlib Plot")
plt.xlabel("X Axis (Numbers)")
plt.ylabel("Y Axis (Doubled)")

plt.show()
