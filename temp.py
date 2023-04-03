import pandas as pd

pokemon = pd.read_csv("data/pokemon.csv", index_col= "Pokemon").squeeze("columns")
print(pokemon.value_counts(normalize = True))