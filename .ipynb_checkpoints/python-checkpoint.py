import pandas as pd
df = pd.read_csv('SNESGames_MobyGames_8-13-2024.csv')

print(df.shape)

# Removing columns with little relevence to scope
df = df.drop(df[df.moby_score == 0].index)
df = df.drop(columns=['id', 'moby_url'])

print(df.shape)