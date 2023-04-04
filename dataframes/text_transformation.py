"""
lower, upper, title and len method
"""
import pandas as pd

chicago = pd.read_csv("data/chicago.csv")
chicago["Department"] = chicago["Department"].astype("category")
t1 = chicago["Name"].str.title()
t2 = chicago["Name"].str.title().str.upper()
print(t2)

"""
replace method
"""
import pandas as pd

chicago = pd.read_csv("data/chicago.csv").dropna(how='all')
chicago["Department"] = chicago["Department"].astype("category")
chicago["Employee Annual Salary"] = chicago["Employee Annual Salary"].str.replace("$", "").astype(float)
print(chicago)

"""
filter method
"""
import pandas as pd

chicago = pd.read_csv("data/chicago.csv").dropna(how='all')
chicago["Department"] = chicago["Department"].astype("category")

f1 = chicago["Position Title"].str.lower().str.contains("water")
f2 = chicago["Position Title"].str.lower().str.startswith("water")
f3 = chicago["Position Title"].str.lower().str.endswith("ist")
print(chicago[f3])

"""
strip, lstrip and rstrip method
"""
import pandas as pd

chicago = pd.read_csv("data/chicago.csv").dropna(how='all')
chicago["Department"] = chicago["Department"].astype("category")

chicago["Name"] = chicago["Name"].str.rstrip().str.lstrip()
chicago["Position Title"] = chicago["Position Title"].str.strip()
chicago.columns = chicago.columns.str.upper()
print(chicago)

"""
split method
"""
import pandas as pd

chicago = pd.read_csv("data/chicago.csv").dropna(how='all')
chicago["Department"] = chicago["Department"].astype("category")
chicago[["First Name", "Last Name"]] = chicago["Name"].str.split(",", expand=True)
print(chicago)