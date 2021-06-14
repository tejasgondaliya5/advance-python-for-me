from datetime import datetime
dt = datetime.today()
print(dt)
print()

newd1 = dt.strftime("%d-%m-%Y")
print(newd1)
print()

newd2 = dt.strftime("%d %B %Y")
print(newd2)
print()

newd3 = dt.strftime("%d/%b/%Y")
print(newd3)
print()

newd4 = dt.strftime("%H:%M:%S")
print(newd4)
print()

newd5 = dt.strftime("%I:%M:%S")
print(newd5)