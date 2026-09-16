from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier

# Text data and labels (1 = Spam, 0 = Normal)
X_text = ["Get free cash now", "Hi, are we meeting today?", "Claim your free prize", "Hey friend, how are you?"]
y = [1, 0, 1, 0]

# Convert text to numbers and train
X = CountVectorizer().fit_transform(X_text)
model = DecisionTreeClassifier().fit(X, y)

# Predict a new email
print("Prediction:", model.predict(CountVectorizer().fit(X_text).transform(["Get your free cash"])))
