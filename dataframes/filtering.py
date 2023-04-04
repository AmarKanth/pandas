"""
Memory Optimization
"""
import pandas as pd

nba = pd.read_csv("data/employees.csv", parse_dates=["Start Date", "Last Login Time"])
nba["Senior Management"] = nba["Senior Management"].astype(bool)
nba["Gender"] = nba["Gender"].astype("category")
print(nba.info())

"""
Multiple Conditional Rendering
"""
import pandas as pd

nba = pd.read_csv("data/employees.csv", parse_dates=["Start Date", "Last Login Time"])
nba["Senior Management"] = nba["Senior Management"].astype(bool)
nba["Gender"] = nba["Gender"].astype("category")

filter_1 = nba["Gender"] == "Male"
filter_2 = nba["Team"] == "Finance"
print(nba[filter_1 & filter_2])

filter_3 = nba["First Name"] == "Robert"
filter_4 = nba["Team"] == "Client Services"
filter_5 = nba["Start Date"] > "2016-06-01"

print(nba[(filter_3 & filter_4) | filter_5])

"""
isin Method
"""
import pandas as pd

nba = pd.read_csv("data/employees.csv", parse_dates=["Start Date", "Last Login Time"])
nba["Senior Management"] = nba["Senior Management"].astype(bool)
nba["Gender"] = nba["Gender"].astype("category")

filter1 = nba["Team"] == "Legal"
filter2 = nba["Team"] == "Sales"
filter3 = nba["Team"] == "Product"
print(nba[filter1 | filter2 | filter3])

isin_filter = nba["Team"].isin(["Legal", "Sales", "Product"])
print(nba[isin_filter])

"""
Range of values
"""
import pandas as pd

nba = pd.read_csv("data/employees.csv", parse_dates=["Start Date", "Last Login Time"])
nba["Senior Management"] = nba["Senior Management"].astype(bool)
nba["Gender"] = nba["Gender"].astype("category")

filter_salary = nba["Salary"].between(60000, 70000)
filter_bonus = nba["Bonus %"].between(2.0, 5.0)
filter_start_date = nba["Start Date"].between("1991-01-01", "1992-01-01")
filter_last_login = nba["Last Login Time"].between("08:30AM", "12:00PM")
print(nba[filter_last_login])

"""
duplicate method
1. returns the list of duplicate values.
"""
import pandas as pd

nba = pd.read_csv("data/employees.csv", parse_dates=["Start Date", "Last Login Time"])
nba["Senior Management"] = nba["Senior Management"].astype(bool)
nba["Gender"] = nba["Gender"].astype("category")
nba.sort_values("First Name", inplace=True)
d1 = nba["First Name"].duplicated(keep='first')
d2 = nba["First Name"].duplicated(keep="last")
d3 = nba["First Name"].duplicated(keep=False)
d4 = -d1
d5 =-d3
print(nba[d5])

"""
drop_duplicates Method
"""
import pandas as pd

nba = pd.read_csv("data/employees.csv", parse_dates=["Start Date", "Last Login Time"])
nba["Senior Management"] = nba["Senior Management"].astype(bool)
nba["Gender"] = nba["Gender"].astype("category")
nba.sort_values("First Name", inplace=True)
d1 = nba.drop_duplicates(subset=["First Name"], keep="first")
d2 = nba.drop_duplicates(subset=["First Name"], keep="last")
d3 = nba.drop_duplicates(subset=["First Name"], keep=False)
d4 = nba.drop_duplicates(subset=["First Name", "Team"])
print(d4)

"""
unique & nunique Method
"""
import pandas as pd

nba = pd.read_csv("data/employees.csv", parse_dates=["Start Date", "Last Login Time"])
nba["Senior Management"] = nba["Senior Management"].astype(bool)
nba["Gender"] = nba["Gender"].astype("category")
nba.sort_values("First Name", inplace=True)
u1 = nba["Team"].unique()
u2 = nba["Team"].nunique()
u3 = nba["Team"].nunique(dropna=False)
print(u3)