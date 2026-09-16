from sklearn.ensemble import GradientBoostingClassifier

# Target labels
X=[
    [1],[2],[3],[4],[5]
]
y = [
    "Fail",
    "Fail",
    "Pass",
    "Pass",
    "Pass"
]

# Create Gradient Boosting model
model = GradientBoostingClassifier(
    n_estimators=10,
    learning_rate=0.1,
    max_depth=2,
    random_state=42
)

# Train the model
model.fit(X, y)
result=model.predict([[2.5]])
print (result[0])


'''
decision  tree 1
        |
        v
find mistake
        |
        v
decisiion tree 2
        |
        v
        

'''