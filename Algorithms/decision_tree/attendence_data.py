from sklearn.tree import DecisionTreeClassifier

x=[
    [90],
    [85],
    [80],
    [55],
    [50]
]

y=["pass","pass","pass","fail","fail"]

model=DecisionTreeClassifier()

model.fit(x,y)

res=model.predict([[67]])
print(res[0])