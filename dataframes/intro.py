"""
1. Series is a one dimentional data stracture(single column).
2. dataframe is two dimentional data stracture(consist of rows and columns)
"""
import pandas as pd
nba = pd.read_csv("data/nba.csv")
print(nba.shape)
print(nba.columns)
print(nba.axes)
print(nba.info())
print(nba.Name)

import pandas as pd
revenue = pd.read_csv("data/revenue.csv", index_col="Date")
print(revenue.sum())
print(revenue.sum(axis="index"))
print(revenue.sum(axis=0))
print(revenue.sum(axis="columns"))
print(revenue.sum(axis=1))

"""
Extracting the columns
"""
import pandas as pd
nba = pd.read_csv("data/nba.csv")
print(nba[["Name", "Team"]])
print(nba["Age"].value_counts())

"""
Creating Columns
"""
import pandas as pd
nba = pd.read_csv("data/nba.csv")
nba["Sport"] = "BasketBall"
nba["Age in a Decade"] = nba["Age"] + 10
nba.insert(loc=2, column="Sport", value="BasketBall")
print(nba.head())

"""
Drop Columns
"""
import pandas as pd
nba = pd.read_csv("data/nba.csv")
print(nba.dropna())
print(nba.dropna(how="any"))
print(nba.dropna(how="all"))
print(nba.dropna(subset=["College", "Salary"]))

"""
Fill in Missing Data
"""
import pandas as pd
nba = pd.read_csv("data/nba.csv")
print(nba.fillna(0))
print(nba["College"].fillna("Unknown"))
nba["College"].fillna("Unknown", inplace=True)
print(nba)
nba["College"] = nba["College"].fillna("Unknown")
print(nba)

"""
astype
"""
import pandas as pd
nba = pd.read_csv("data/nba.csv").dropna(how="all")
nba["Age"] = nba["Age"].astype(int)
print(nba)

import pandas as pd
nba = pd.read_csv("data/nba.csv")
nba["Age"] = nba["Age"].fillna(0)
nba["Age"] = nba["Age"].astype(int)
print(nba)
print(nba["Position"].nunique())
print(nba["Position"].astype("category"))

"""
sort_values
"""
import pandas as pd

nba = pd.read_csv("data/nba.csv")
sort_by_name = nba.sort_values(by="Name", ascending=False)
sort_by_salary = nba.sort_values(by="Salary", na_position="first", ascending=False)
sort_by_team_and_name = nba.sort_values(by=["Team", "Name"], ascending=[False, True])
print(sort_by_team_and_name)

"""
sort_index
"""
import pandas as pd

nba = pd.read_csv("data/nba.csv")
sort_by_inex = nba.sort_index(ascending=False)
print(sort_by_inex)

"""
rank method
"""
import pandas as pd

nba = pd.read_csv("data/nba.csv")
nba["Salary"] = nba["Salary"].fillna(0)
nba["Salary Rank"] = nba["Salary"].rank(ascending=False).astype("int")
print(nba.sort_values(by="Salary", ascending=False))