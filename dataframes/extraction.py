"""
set_index and reset_indx methods
"""
import pandas as pd

bond = pd.read_csv("python/pandas/data/jamesbond.csv")
bond.set_index(keys='Film', inplace=True)
r1 = bond.reset_index()
r2 = bond.reset_index(drop=True)
r3 = bond.reset_index(drop=False, inplace=True)
print(bond)

"""
loc Accessor
"""
import pandas as pd

bond = pd.read_csv("Projects/python/pandas/data/jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)
l1 = bond.loc["Goldfinger"]
l2 = bond.loc["GoldenEye"]
l3 = bond.loc["Casino Royale"]
l4 = bond.loc["Daimonds Are Forever":"From Russia with Love"]
l5 = bond.loc["Daimonds Are Forever":"From Russia with Love":2]
l6 = bond.loc["GoldenEye":]
l7 = bond.loc[:"On Her Majesty's Secret Service"]
l8 = bond.loc[["Die Another Day", "Octopussy"]]
l9 = bond.loc[["Octopussy", "Die Another Day"]]
l10 = "Gold Bond" in bond.index
print(l8)

"""
iloc Accessor
"""
import pandas as pd

bond = pd.read_csv("python/pandas/data/jamesbond.csv")
bond.set_index("Film", inplace=True)
bond.sort_index()
l1 = bond.iloc[0]
l2 = bond.iloc[15]
l3 = bond.iloc[[0,15]]
l4 = bond.iloc[4:8]
l5 = bond.iloc[20:]
l6 = bond.iloc[:4]
print(l6)

"""
loc and iloc Accessor with second argument
"""
import pandas as pd

bond = pd.read_csv("python/pandas/data/jamesbond.csv")
bond.set_index("Film", inplace=True)
bond.sort_index()
l1 = bond.loc["Moonraker", "Actor"]
l2 = bond.loc["Moonraker", ["Actor", "Director"]]
l3 = bond.loc[["Moonraker", "A View to a Kill"], ["Actor", "Director"]]
l4 = bond.loc["Moonraker", "Director":"Budget"]
l5 = bond.loc["Moonraker":"A View to a Kill", "Director":"Budget"]
l6 = bond.loc["Moonraker":, "Director":"Budget"]
l7 = bond.loc["Moonraker":, "Director":]
l8 = bond.loc[:"Moonraker", :"Director"]

il1 = bond.iloc[14, 2]
il2 = bond.iloc[14, 2:5]
il3 = bond.iloc[[14,17], [2,4]]
il4 = bond.iloc[:7, [2,4]]
il5 = bond.iloc[:7, :3]
print(il5)

"""
Replace row or cell values with loc and iloc Accessor
"""
import pandas as pd

bond = pd.read_csv("python/pandas/data/jamesbond.csv")
bond.set_index("Film", inplace=True)
bond.sort_index()
bond.loc["Dr. No", "Actor"] = "Sir Sean Connery"
bond.loc["Dr. No", ["Box Offic", "Budget", "Bond Actor Salary"]] = [448000000, 7000000, 600000]
print(bond)

"""
Set Multiple values in df
"""
import pandas as pd

bond = pd.read_csv("python/pandas/data/jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)
actor_is_sean_connery = bond["Actor"] == "Sean Connery"
bond.loc[actor_is_sean_connery, "Actor"] = "Sir Sean Connery"
print(bond)

"""
Renaming column names
"""
import pandas as pd

bond = pd.read_csv("python/pandas/data/jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)
r1 = bond.rename(
    mapper={"GoldenEye": "Golden Eye", "The World Is Not Enough": "Best Bond Movie Ever"}, 
    axis=0
    )
r2 = bond.rename(
    mapper={"GoldenEye": "Golden Eye", "The World Is Not Enough": "Best Bond Movie Ever"}, 
    axis="rows"
    )
r3 = bond.rename(
    mapper={"GoldenEye": "Golden Eye", "The World Is Not Enough": "Best Bond Movie Ever"}, 
    axis="index"
    )
r4 = bond.rename(
    index={"GoldenEye": "Golden Eye", "The World Is Not Enough": "Best Bond Movie Ever"}
    )
r5 = bond.rename(
    index={"GoldenEye": "Golden Eye", "The World Is Not Enough": "Best Bond Movie Ever"},
    inplace=True
    )

c1 = bond.rename(
    mapper={"Year": "Release Date", "Box Office": "Revenue"},
    axis=1
)
c2 = bond.rename(
    mapper={"Year": "Release Date", "Box Office": "Revenue"},
    axis="columns"
)
c3 = bond.rename(
    columns={"Year": "Release Date", "Box Office": "Revenue"}
)
c4 = bond.rename(
    columns={"Year": "Release Date", "Box Office": "Revenue"},
    inplace=True
)
c5 = bond.columns
bond.columns = ["Year of Release", "Actor", "Director", "Gross", "Cost", "Salary"]
print(bond)

"""
delete rows or columns from df
"""
import pandas as pd

bond = pd.read_csv("Projects/python/pandas/data/jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)
d1 = bond.drop(["A View to a Kill", "Die Another Day", "From Russia with Love"])
d2 = bond.drop("Casino Royale", inplace=True)
d3 = bond.drop("Box Office", axis="columns")
d4 = bond.drop(["Box Office", "Bond Actor Salary", "Actor"], axis="columns", inplace=True)
d5 = bond.pop("Actor")
del bond["Director"]
print(bond)

"""
create random sample
"""
import pandas as pd

bond = pd.read_csv("Projects/python/pandas/data/jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)
s1 = bond.sample()
r1 = bond.sample(n=5)
r2 = bond.sample(n=3, axis="index")
c1 = bond.sample(n=3, axis=1)
c2 = bond.sample(n=3, axis="columns")
print(c2)

"""
nsmallest and nlargest methods
"""
import pandas as pd

bond = pd.read_csv("Projects/python/pandas/data/jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)
nl1 = bond.nlargest(3, columns="Box Office")
nl2 = bond["Box Office"].nlargest(3)
ns1 = bond.nsmallest(3, columns="Box Office")
ns2 = bond["Box Office"].nsmallest(3)
print(ns2)

"""
where method
"""
import pandas as pd

bond = pd.read_csv("Projects/python/pandas/data/jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)
condition1 = bond["Actor"] == "Sean Connery"
condition2 = bond["Box Office"] > 800
w1 = bond.where(condition1)
w2 = bond.where(condition1 & condition2)
print(w2)

"""
query method
"""
import pandas as pd

bond = pd.read_csv("Projects/python/pandas/data/jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)
bond.columns = [column_name.replace(" ", "_") for column_name in bond.columns]
q1 = bond.query('Actor == "Sean Connery"')
q2 = bond.query('Director == "Terence Young"')
q3 = bond.query('Actor != "Roger Moore"')
q4 = bond.query('Actor == "Roger Moore" and Director == "John Glen"')
q5 = bond.query('Actor == "Roger Moore" or Director == "John Glen"')
q6 = bond.query('Actor in ["Timothy Dalton", "George Lazenby"]')
q7 = bond.query('Actor not in ["Sean Connery", "Roger Moore"]')
print(q7)

"""
apply method
"""
import pandas as pd

bond = pd.read_csv("Projects/python/pandas/data/jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)

def convert_to_string_and_add_millions(number):
    return str(number) + " Millions!"

columns = ["Box Office", "Budget", "Bond Actor Salary"]
for col in columns:
    bond[col] = bond[col].apply(convert_to_string_and_add_millions)
print(bond)

def good_movie(row):
    actor = row[1]
    budget = row[4]
    if actor == "Pierce Brosnan":
        return "The Best"
    elif actor == "Roger Moore" and budget > 40:
        return "Enjoyable"
    else:
        return "I have no clue"

a1 = bond.apply(good_movie, axis="columns")
print(a1)

"""
copy method
"""
import pandas as pd

bond = pd.read_csv("python/pandas/data/jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)
directors = bond["Director"].copy()
directors["A View to a Kill"] = "Mister John Glen"
print(directors)