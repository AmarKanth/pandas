"""
group by Method
"""
import pandas as pd

fortune = pd.read_csv("pandas/data/fortune1000.csv", index_col="Rank")
sectors = fortune.groupby("Sector")
g1 = sectors.first()
g2 = sectors.last()
g3 = sectors.groups
print(g3)

"""
get_group by Method
"""
import pandas as pd

fortune = pd.read_csv("pandas/data/fortune1000.csv", index_col="Rank")
sectors = fortune.groupby("Sector")
g1 = sectors.get_group("Energy")
g2 = fortune[fortune["Sector"] == "Energy"]
g3 = sectors.max()
g4 = sectors.min()
g5 = sectors.sum()
g6 = sectors.get_group("Apparel")["Revenue"].sum()
g7 = sectors.mean()
g8 = sectors["Revenue"].sum()
g9 = sectors[["Revenue", "Profits"]].sum()
print(g9)

"""
group by on Muliple columns
"""
import pandas as pd

fortune = pd.read_csv("pandas/data/fortune1000.csv", index_col="Rank")
sectors = fortune.groupby(["Sector", "Industry"])
g1 = sectors.size()
g2 = sectors.sum()
g3 = sectors["Revenue"].sum()
g4 = sectors["Employees"].mean()
print(g4)

"""
agg method
"""
import pandas as pd

fortune = pd.read_csv("pandas/data/fortune1000.csv", index_col="Rank")
sectors = fortune.groupby("Sector")
g1 = sectors.agg({"Revenue": "sum", "Profits": "sum", "Employees": "mean"})
g2 = sectors.agg(["size", "sum", "mean"])
g3 = sectors.agg({"Revenue": ["sum", "mean"], "Profits": "sum", "Employees": "mean"})
print(g3)

"""
iterating through groups
"""
import pandas as pd

fortune = pd.read_csv("pandas/data/fortune1000.csv", index_col="Rank")
sectors = fortune.groupby("Sector")
df = pd.DataFrame(columns=fortune.columns)
for sector, data in sectors:
    highest_revenue_company_in_group = data.nlargest(1, "Revenue")
    df = df.append(highest_revenue_company_in_group)
print(df)