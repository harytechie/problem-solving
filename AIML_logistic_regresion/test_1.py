import pandas as pd
from sklearn.linear_model import LogisticRegression
X = [
    [5.5, 4],
    [5.8, 5],
    [6.0, 4],
    [6.2, 5],
    [6.5, 6]
]
y = [0, 0, 0, 1, 1]
model = LogisticRegression()
model.fit(X, y)
result = model.predict(X)

print("CGPA | Interview | Selected")

for i in range(len(X)):
    print(X[i][0], " | ", X[i][1], "       | ", result[i])
cgpa = float(input("Enter CGPA: "))
interview = int(input("Enter Interview Score: "))
prediction = model.predict([[cgpa, interview]])

if prediction[0] == 1:
    print("Selected")
else:
    print("Not Selected")