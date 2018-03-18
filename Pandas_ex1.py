"""Data frame is a main object in Pandas.
It is used to represent data with rows and columns"""

import pandas
us_wars_by_end = { 'day' : ['1/2/2007', '1/2/2007', '1/3/2007'],
                   'temperature': [32, 35, 28],
                   'wind speed': [6, 7, 2],
                   'event': ['Rain', 'Sunny', 'Snow']}
df = pandas.DataFrame(us_wars_by_end)
print(df)
print(df.columns)
print(df.event)