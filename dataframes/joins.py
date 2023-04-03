"""
pd.concat Method
"""
import pandas as pd

week1 = pd.read_csv("pandas/data/Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("pandas/data/Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("pandas/data/Restaurant - Customers.csv")
foods = pd.read_csv("pandas/data/Restaurant - Foods.csv")
week = pd.concat(objs=[week1, week2], ignore_index=True)
week_alt = week1.append(other=week2, ignore_index=True)
sales = pd.concat(objs=[week1, week2], keys=["Week1", "Week2"])
w1 = sales.loc[("Week1",)]
w2 = sales.loc[("Week2",)]
s1 = sales.loc[("Week1", 240)]
s2 = sales.loc[("Week1", 240), "Customer ID"]
s3 = sales.loc[("Week1", 240), ["Customer ID", "Food ID"]]
print(s3)

"""
Inner Joins
"""
import pandas as pd

week1 = pd.read_csv("pandas/data/Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("pandas/data/Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("pandas/data/Restaurant - Customers.csv")
foods = pd.read_csv("pandas/data/Restaurant - Foods.csv")
innerjoin1 = week1.merge(week2, how="inner", on="Customer ID", suffixes=[" - Week 1", " - Week 2"])
innerjoin2 = week1.merge(week2, how="inner", on=["Customer ID", "Food ID"])
print(innerjoin2)

"""
Outer Joins
"""
import pandas as pd

week1 = pd.read_csv("pandas/data/Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("pandas/data/Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("pandas/data/Restaurant - Customers.csv")
foods = pd.read_csv("pandas/data/Restaurant - Foods.csv")
outerjoin = week1.merge(week2, how="outer", on="Customer ID")
merged = week1.merge(week2, how="outer", on="Customer ID", suffixes=[" - Week 1", " - Week 2"], indicator=True)
condition = merged["_merge"].isin(["left_only", "right_only"])
fullouter = merged[condition]
print(fullouter)

"""
Left Joins
"""
import pandas as pd

week1 = pd.read_csv("pandas/data/Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("pandas/data/Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("pandas/data/Restaurant - Customers.csv")
foods = pd.read_csv("pandas/data/Restaurant - Foods.csv")
leftjoin = week1.merge(foods, how="left", on="Food ID", sort=True)
print(leftjoin)

"""
left_on and right_on parameter
"""
import pandas as pd

week1 = pd.read_csv("pandas/data/Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("pandas/data/Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("pandas/data/Restaurant - Customers.csv")
foods = pd.read_csv("pandas/data/Restaurant - Foods.csv")
join = week2.merge(customers, how="left", left_on="Customer ID", right_on="ID", sort=True).drop("ID", axis="columns")
print(join)

"""
left_index and right_index parameter
"""
import pandas as pd

week1 = pd.read_csv("pandas/data/Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("pandas/data/Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("pandas/data/Restaurant - Customers.csv", index_col="ID")
foods = pd.read_csv("pandas/data/Restaurant - Foods.csv", index_col="Food ID")
sales = week1.merge(customers, how="left", left_on="Customer ID", right_index=True)
sales = sales.merge(foods, how="left", left_on="Food ID", right_index=True)
print(sales)

"""
join method
"""
import pandas as pd

week1 = pd.read_csv("pandas/data/Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("pandas/data/Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("pandas/data/Restaurant - Customers.csv", index_col="ID")
foods = pd.read_csv("pandas/data/Restaurant - Foods.csv", index_col="Food ID")
rating = pd.read_csv("pandas/data/Restaurant - Week 1 Satisfaction.csv")
j1 = week1.join(rating)
print(j1)

"""
merge method
"""
import pandas as pd

week1 = pd.read_csv("pandas/data/Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("pandas/data/Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("pandas/data/Restaurant - Customers.csv", index_col="ID")
foods = pd.read_csv("pandas/data/Restaurant - Foods.csv", index_col="Food ID")
rating = pd.read_csv("pandas/data/Restaurant - Week 1 Satisfaction.csv")
join = pd.merge(week1, customers, how="left", left_on="Customer ID", right_on="ID")
print(join)