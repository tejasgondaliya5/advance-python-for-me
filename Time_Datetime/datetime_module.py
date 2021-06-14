from datetime import datetime

# print(dir(datetime))
dt = datetime(year=2021, month=5, day=12)                                 # "dt" is object for date class
dt1 = datetime(year=2021, month=5, day=12, hour=15, minute=10, second=45)
print(dt)
print(dt1)

ct = datetime.now()
print(ct)
print(ct.day)
print(ct.month)
print(ct.year)
