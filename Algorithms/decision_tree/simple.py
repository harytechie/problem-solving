from sklearn.tree import DecisionTreeClassifier as tree

x=[
    [100],
    [80],
    [60],
    [50],
]
y=['pass','pass','pass','fail']

model=tree()
model.fit(x,y)
result=model.predict([[50]])
print(result[0])