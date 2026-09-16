from sklearn.metrics import accuracy_score

y_test=[
    "Spam",
    "Not Spam",
    "Spam",
    "not Spam",
    "Spam",
    "Not Spam",
    "Spam",
    "not Spam",
    "Spam",
    "Not Spam",
    "Spam",
    "not Spam",
    ]

knn_pred = [
    "Spam", "Not Spam", "Spam", "not Spam", "Spam", "Not Spam",
    "Spam", "Spam", "Spam", "Not Spam", "Spam", "not Spam",
]

dt_pred = [
    "Spam", "Not Spam", "Spam", "not Spam", "Not Spam", "Not Spam",
    "Spam", "not Spam", "Spam", "Not Spam", "Spam", "not Spam",
]

rf_pred = [
    "Spam", "Not Spam", "Spam", "not Spam", "Spam", "Not Spam",
    "Spam", "not Spam", "Spam", "Not Spam", "Spam", "not Spam",
]

knn_a=accuracy_score(y_test, knn_pred)
dt_a=accuracy_score(y_test, dt_pred)
rf_a=accuracy_score(y_test, rf_pred)


print("KNN Accuracy:", knn_a * 100, "%")
print("Decision Tree Accuracy:", dt_a * 100, "%")
print("Random Forest Accuracy:", rf_a * 100, "%")
