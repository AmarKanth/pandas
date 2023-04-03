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
pandas_reader library
"""
import pandas as pd
import datetime as dt
import yfinance as yf

from pandas_datareader import data

yf.pdr_override()
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2020, 12, 31)

stocks = data.get_data_yahoo("MSFT", start, end)
t1 = stocks.loc[pd.Timestamp("2010-01-04")]
t2 = stocks.loc[[pd.Timestamp("2010-01-04"), pd.Timestamp("2010-01-05")]]
dates = pd.date_range(start="1991-04-12", end="2020-12-31", freq=pd.DateOffset(years=1))
available_dates = stocks.index.isin(dates)
print(stocks.loc[available_dates])

"""
DateOffset Object
"""
import pandas as pd
import datetime as dt
import yfinance as yf

from pandas_datareader import data

yf.pdr_override()
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2020, 12, 31)

stocks = data.get_data_yahoo("MSFT", start, end)
offset = stocks.index + pd.DateOffset(days=5)
print(offset)

"""
Timeseries Object
"""
import pandas as pd
import datetime as dt
import yfinance as yf

from pandas_datareader import data

yf.pdr_override()
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2020, 12, 31)

stocks = data.get_data_yahoo("MSFT", start, end)
offset = stocks.index + pd.tseries.offsets.MonthEnd()
print(offset)

"""
Timedelta Object
"""
import pandas as pd
import datetime as dt
import yfinance as yf

from pandas_datareader import data

yf.pdr_override()
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2020, 12, 31)

stocks = data.get_data_yahoo("MSFT", start, end)

time_a = pd.Timestamp("2020-03-31")
time_b = pd.Timestamp("2020-03-20")
print(time_a-time_b)