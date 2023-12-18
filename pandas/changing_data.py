import pandas as pd

df = pd.read_csv('data/pokemon_data.csv')

## adding a column
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

## dropping a column
df = df.drop(columns=['Total'])

## adding a column with a different method
df['Total'] = df.iloc[:, 4:10].sum(axis=1)

## cols
cols = list(df.columns.values)

## reordering columns
##df = df[cols[0:11] + [cols[-1]] + [cols[11]]]
##print(df.head(5))