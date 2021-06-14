# a+ method is first append the data then read data.

f = open('append+method', 'a+')
# append method can not overwrite data
f.write('How are you.\n')

f.seek(0)
data = f.read()
print(data)
