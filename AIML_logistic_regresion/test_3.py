from sklearn.neighbors import KNeighborsClassifier

X = [
    [1, 4],
    [2, 5],
    [2, 6],
    [3, 5],
    [3, 7]
]

y = [0, 0, 0, 0, 1]

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X, y)

experience = float(input("Enter Years of Experience: "))
performance = float(input("Enter Performance Score: "))

prediction = model.predict([[experience, performance]])

if prediction[0] == 1:
    print("Promoted")
else:
    print("Not Promoted")