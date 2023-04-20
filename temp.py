import pandas as pd

fortune = pd.read_csv("data/fortune1000.csv", index_col="Rank")
sectors = fortune.groupby("Sector")
df = pd.DataFrame(columns=fortune.columns)

for sector, data in sectors:
    nlargest_by_revenue = data.nlargest(1, "Revenue")
    df = pd.concat([df, nlargest_by_revenue])

print(df)