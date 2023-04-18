import pandas as pd

week1 = pd.read_csv("data/Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("data/Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("data/Restaurant - Customers.csv")
foods = pd.read_csv("data/Restaurant - Foods.csv")

sales = pd.concat(objs=[week1, week2], keys=["Week1", "Week2"])
s3 = sales.loc[("Week1", 240), ["Customer ID", "Food ID"]]
print(s3)