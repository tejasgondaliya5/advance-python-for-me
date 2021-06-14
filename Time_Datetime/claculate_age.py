from datetime import date

DOB = date(2000, 6, 12)
t1 = date.today()

age = t1.year - DOB.year - ((t1.month,t1.day) < (DOB.month, DOB.day))
print(age)
