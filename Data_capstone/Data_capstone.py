import numpy as np
import pandas as pd

df = pd.read_csv('Countries.csv')

# Capital city of the most populated country
a = df[df['population'] == df['population'].max()]['capital_city']

# Capital city of the least populated country
b = df[df['population'] == df['population'].min()]['capital_city']

# Sort by democracy score
df.sort_values(by='democracy_score', ascending=False, inplace=True)

# Top 5 countries by democracy score
c = df['country'].head()
print(c)

# Count countries in each region
d = df['region'].value_counts()

# Number of unique regions
e = df['region'].value_counts().count()
# or
# e = df['region'].nunique()

# Number of countries in Eastern Europe
f = df['region'].value_counts()['Eastern Europe']

# All countries in Eastern Europe
h = df[df['region'] == 'Eastern Europe']['country']
g = df[df['population'] == df['population'].nlargest(2).iloc[1]]
i = df[df['political_leader'].isna()]['country']
print(d)
print(e)
print(f)
print(h)
print(g)
print(i)