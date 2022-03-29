import datetime
import pytz
import csv
# print(pytz.timezone("US/Eastern"))
# my_date = datetime.datetime.now(pytz.timezone('US/Pacific'))
utc = datetime.datetime.utcnow() # utc time
locale = datetime.datetime.now() # system time
pol_utc = datetime.timedelta(hours=2)
poland = utc +pol_utc #summer timezone in Poland

with open("data.csv","a") as daty:
    outputWriter = csv.writer(daty)
    outputWriter.writerow([str(poland)])
    
"""Pandas approach"""
import datetime
import pytz
import pandas as pd
my_date = datetime.datetime.now(pytz.timezone('Poland'))
# now = datetime.datetime.today()
df = pd.DataFrame({
    "data": [my_date]})

df.to_csv("data.csv", index=False, mode="a", header=False)