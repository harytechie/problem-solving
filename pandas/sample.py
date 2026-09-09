import pandas as pd

df = pd.DataFrame([1,2,3,4,5])

column_totals = df.sum()  
print(column_totals)

# row_totals = df.sum(axis=1)  

# column_a_total = df['A'].sum() 

# grand_total = df.sum().sum()  
