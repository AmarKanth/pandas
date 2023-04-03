import pandas as pd
res = pd.read_csv("data/pokemon.csv", index_col="Pokemon").squeeze("columns")
print(res)