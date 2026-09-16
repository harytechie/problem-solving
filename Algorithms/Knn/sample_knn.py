from sklearn. neighbors import KNeighborsClassifier as knn
x = [[150], [155], [160], [175], [180], [185]]
y = ["Short", "Short", "Short", "Tall", "Tall", "Tall"]

model = knn(n_neighbors=4)
model.fit(x, y)

result = model.predict([[170]])
print(result[0])