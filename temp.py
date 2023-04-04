import pandas as pd

bond = pd.read_csv("data/jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)
condition1 = bond["Actor"] == "Sean Connery"
condition2 = bond["Box Office"] > 800
print(bond.where(condition1 & condition2).dropna())