from sklearn.linear_model import LogisticRegression

X = [
    [20, 500],
    [25, 520],
    [30, 550],
    [35, 580],
    [50, 650],
    [60, 700],
    [70, 750],
    [80, 800]
]

y = [0, 0, 0, 0, 1, 1, 1, 1]

model = LogisticRegression()

model.fit(X, y)

income = float(input("Enter Income: "))
credit = float(input("Enter Credit Score: "))

prediction = model.predict([[income, credit]])

if prediction[0] == 1:
    print("Approved")
else:
    print("Rejected")