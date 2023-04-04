import pandas as pd

nba = pd.read_csv("data/nba.csv")
nba["Salary"] = nba["Salary"].fillna(0)
nba["Salary Rank"] = nba["Salary"].rank(ascending=False).astype("int")
print(nba.sort_values(by="Salary Rank").tail(20))