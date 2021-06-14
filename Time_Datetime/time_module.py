from time import time, ctime, localtime
# using time module
epoch = time()
print(epoch)

# using ctime module
et = ctime()
print(et)

print(ctime())

# this is localtime module used   "....this module is most of used...."
stobj = localtime()
print(stobj)
print()

print("date is :", stobj.tm_mday, end="/")
print(stobj.tm_mon, end="/")
print(stobj.tm_year)
print()

print("time is :", stobj.tm_hour, end=":")
print(stobj.tm_min, end=":")
print(stobj.tm_sec)

