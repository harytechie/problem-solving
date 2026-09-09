from sklearn. tree import DecisionTreeClassifier

x=[
    [90,100],
    [85,90],
    [80,60],
    [55,40],
    [50,30]
]

y=["pass","pass","pass","fail","fail"]

model=DecisionTreeClassifier()

model.fit(x,y)

res=model.predict([[100,67]])
print(res[0])