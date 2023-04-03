"""
to_datetime method
"""
import pandas as pd
dates = pd.Series(["July 4th, 1996", "10/04/1991", "Hello", "2015-02-31"])
d1 = pd.to_datetime(dates, errors="coerce")
d2 = pd.to_datetime([1349720105, 1349806505, 1349892905, 1350065705], unit="s")
print(d2)

"""
date_range method
"""
import pandas as pd
times = pd.date_range(start="2016-01-01", end="2016-01-10", freq="D")
b = pd.date_range(start="2016-01-01", end="2016-01-15", freq="B")
w = pd.date_range(start="2016-01-01", end="2016-01-15", freq="W")
w_fri = pd.date_range(start="2016-01-01", end="2016-01-15", freq="W-FRI")
h = pd.date_range(start="2016-01-01", end="2016-01-15", freq="H")
h6 = pd.date_range(start="2016-01-01", end="2016-01-15", freq="6H")
m = pd.date_range(start="2016-01-01", end="2016-12-31", freq="M")
d = pd.date_range(start="2016-01-01", end="2016-12-31", freq="D")
b = pd.date_range(start="2016-01-01", periods=50, freq="B")
e = b = pd.date_range(end="1999-12-31", periods=20, freq="D")
print(b)

"""
.dt Accessor
"""
import pandas as pd
times = pd.date_range(start="2016-01-01", end="2016-12-31", freq="D")
series = pd.Series(times)
dt1 = series.dt.day
dt2 = series.dt.is_quarter_start
print(dt2)

"""
Date Offset
"""
import pandas as pd

date = pd.Timestamp("2019-10-10 07:15:11")
offset1 = pd.tseries.offsets.DateOffset(n=2)
offset2 = pd.tseries.offsets.DateOffset(days=10, hours=2)
offset3 = pd.tseries.offsets.MonthEnd()
print(date)
print(date+offset2)