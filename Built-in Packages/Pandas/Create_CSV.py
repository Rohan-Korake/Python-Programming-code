import pandas as pd

data={
    'Name':['Jerry','Ram','Sita'],
    'Age':[12,17,18],
    'City':['Delhi','Pandharpur','Sangli']
}
df=pd.DataFrame(data)
df.to_csv('Test.csv',index=False)

print("CSV file created successfully......")