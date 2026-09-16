from sklearn.tree import DecisionTreeClassifier

# Training data
X = [
    [22, 25000, 550],
    [25, 30000, 580],
    [30, 50000, 650],
    [35, 60000, 700],
    [40, 75000, 750],
    [45, 80000, 780],
    [28, 40000, 620],
    [32, 55000, 680]
]

# 0 = Reject, 1 = Approve
y = [0, 0, 1, 1, 1, 1, 0, 1]

# Create Decision Tree
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

# New customer
new_customer = [[29, 52000, 670]]

# Prediction
result = model.predict(new_customer)

if result[0] == 1:
    print("Loan: Approve")
else:
    print("Loan: Reject")