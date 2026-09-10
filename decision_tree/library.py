from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
X = [
    [2, 60],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80],
    [7, 85],
    [2, 55],
    [6, 78],
    [3, 62],
    [5, 77]
]
y = [0, 0, 0, 1, 1, 1, 0, 1, 0, 1]
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#Create Decision Tree
model = DecisionTreeClassifier(random_state=42)
# Train
model.fit(X_train, y_train)
# Predict
y_pred = model.predict(X_test)
print("Actual:", y_test)
print("Predicted:", y_pred)
# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
