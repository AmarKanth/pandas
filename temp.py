import pandas as pd

fortune = pd.read_csv("data/fortune1000.csv", index_col="Rank")
sectors = fortune.groupby("Sector")
g1 = sectors.first()
g3 = sectors.groups
print(g3)