from sklearn.linear_model import LogisticRegression

X = [
    [22, 499, 2, 5, 0],
    [45, 799, 36, 1, 1],
    [31, 599, 8, 4, 0],
    [52, 999, 60, 0, 1],
    [28, 699, 5, 6, 0],
    [41, 899, 48, 1, 1],
    [35, 549, 12, 3, 0],
    [60, 799, 72, 0, 1],
]

y = ['leave', 'stay','leave', 'stay','leave', 'stay','leave', 'stay']

model= LogisticRegression()

model.fit(X,y)

result=model.predict([[27, 499, 2, 5, 0]])

print(result[0])
