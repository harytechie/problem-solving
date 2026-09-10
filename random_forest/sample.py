from sklearn.ensemble import RandomForestClassifier

# Each row: [hours_studied, attendance_percentage]
X = [
    [1, 50],
    [2, 60],
    [3, 65],
    [4, 75],
    [5, 85],
    [6, 90],
]

# 0 = fail, 1 = pass
y = [0, 0, 0, 1, 1, 1]

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

student = [[4, 80]]
prediction = model.predict(student)[0]

print("Pass" if prediction == 1 else "Fail")
