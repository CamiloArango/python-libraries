import pandas as pd

df = pd.read_csv('data/pokemon_data.csv')

## Read Headers
df.columns

## Read each Column
df['Name'][0:5]

## Read each Row
df.iloc[1:4]

## Read a specific location (R,C)
df.iloc[2,1]

## Iterate through each row
for index, row in df.iterrows():
    print(index, row['Name'])

## Find specific data
df.loc[df['Type 1'] == "Fire"]

## Sorting/Describing Data
df.describe()

df.sort_values('Name', ascending=False)

df.sort_values(['Type 1', 'HP'], ascending=[1,0])