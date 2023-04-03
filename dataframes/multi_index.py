"""
MultiIndex with set_index
"""
import pandas as pd

bigmac = pd.read_csv("pandas/data/bigmac.csv", parse_dates=["Date"])
m1 = bigmac.set_index(keys=["Date", "Country"])
m2 = bigmac.set_index(keys=["Country", "Date"])
bigmac.set_index(keys=["Date", "Country"], inplace=True)
bigmac.index
bigmac.index.names
print(bigmac.index.names)

"""
Extract Index Level Values with 
get_level_values method
"""
import pandas as pd

bigmac = pd.read_csv("pandas/data/bigmac.csv", parse_dates=["Date"], index_col=["Date", "Country"])
bigmac.sort_index(inplace=True)
g1 = bigmac.index.get_level_values("Date")
g2 = bigmac.index.get_level_values(0)
g3 = bigmac.index.get_level_values(1)
print(g3)

"""
Change index level with set_names method
"""
import pandas as pd

bigmac = pd.read_csv("pandas/data/bigmac.csv", parse_dates=["Date"], index_col=["Date", "Country"])
bigmac.sort_index(inplace=True)
s1 = bigmac.index.set_names(names=["Day", "Location"], inplace=True)
s2 = bigmac.index.set_names(names="Date", level=0)
s3 = bigmac.index.set_names(names="Date", level="Day", inplace=True)
print(bigmac)

"""
sort_index on MultiIndex DF
"""
import pandas as pd

bigmac = pd.read_csv("pandas/data/bigmac.csv", parse_dates=["Date"], index_col=["Date", "Country"])
s1 = bigmac.sort_index(ascending=True)
s2 = bigmac.sort_index(ascending=False)
s3 = bigmac.sort_index(ascending=[True, False])
s4 = bigmac.sort_index(level=1)
s5 = bigmac.sort_index(level="Country", ascending=False)
print(s5)

"""
loc on Multi Index DF
"""
import pandas as pd

bigmac = pd.read_csv("pandas/data/bigmac.csv", parse_dates=["Date"], index_col=["Date", "Country"])
bigmac.sort_index(inplace=True)
l1 = bigmac.loc["2010-01-01", "Argentina"]
l2 = bigmac.loc["2010-01-01", "Price in US Dollars"]
l3 = bigmac.loc[("2010-01-01", "Argentina"), ("Price in US Dollars", "Price in US Dollars")]

l4 = bigmac.iloc[0]
l5 = bigmac.iloc[[10, 20, 30, 250]]
print(l5)

"""
transpose Method
"""
import pandas as pd

bigmac = pd.read_csv("pandas/data/bigmac.csv", parse_dates=["Date"], index_col=["Date", "Country"])
bigmac.sort_index(inplace=True)
t1 = bigmac.transpose()
t2 = t1.loc[("Price in US Dollars",), ("2010-01-01", "Sri Lanka"):("2010-01-01", "Ukraine")]
print(t2)

"""
swaplevel Method
"""
import pandas as pd

bigmac = pd.read_csv("pandas/data/bigmac.csv", parse_dates=["Date"], index_col=["Date", "Country"])
bigmac.sort_index(inplace=True)
s1 = bigmac.swaplevel()
s2 = bigmac.swaplevel("Date", "Country")
s3 = bigmac.swaplevel("Country", "Date")
s4 = bigmac.swaplevel(0,1)
s5 = bigmac.swaplevel(1,0)
bigmac = s5
print(bigmac)

"""
stack Method
"""
import pandas as pd

world = pd.read_csv("pandas/data/worldstats.csv", index_col=["country", "year"])
s1 = world.stack()
s2 = world.stack().to_frame()
print(s2)

"""
unstack Method
"""
import pandas as pd

world = pd.read_csv("pandas/data/worldstats.csv", index_col=["country", "year"])
s = world.stack()
us1 = s.unstack()
us2 = s.unstack().unstack()
us3 = s.unstack().unstack().unstack()
us4 = s.unstack(0)
us5 = s.unstack(1)
us6 = s.unstack(-1)
us7 = s.unstack("country")
us8 = s.unstack(level=[1,0])
us9 = s.unstack(level=[0,1])
us10 = s.unstack(level=["year","country"])
us11 = s.unstack("year", fill_value=0)
print(us11)

"""
pivat Method
"""
import pandas as pd

sales = pd.read_csv("pandas/data/salesmen.csv", parse_dates=["Date"])
sales["Salesman"] = sales["Salesman"].astype("category")
p1 = sales.pivot(index="Date", columns="Salesman", values="Revenue")
print(p1)

"""
pivat_table Method
"""
import pandas as pd

foods = pd.read_csv("pandas/data/foods.csv")
p1 = foods.pivot_table(values="Spend", index="Gender", aggfunc="sum")
p2 = foods.pivot_table(values="Spend", index=["Gender", "Item"], aggfunc="sum")
p3 = foods.pivot_table(values="Spend", index=["Gender", "Item"], columns="City", aggfunc="sum")
p4 = foods.pivot_table(values="Spend", index=["Gender", "Item"], columns=["Frequency","City"], aggfunc="sum")
p5 = pd.pivot_table(data=foods, values="Spend", index=["Gender", "Item"], columns="City", aggfunc="sum")
print(p5)

"""
pd.melt Method
"""
import pandas as pd

sales = pd.read_csv("pandas/data/quarters.csv")
m1 = pd.melt(sales, id_vars="Salesman")
m2 = pd.melt(sales, id_vars="Salesman", var_name="Quarter")
m3 = pd.melt(sales, id_vars="Salesman", var_name="Quarter", value_name="Revenue")
print(m3)