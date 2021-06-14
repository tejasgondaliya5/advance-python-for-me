from datetime import timedelta, date

td1 = timedelta(days=10)
d = date.today()
print(d + td1)
print(d - td1)