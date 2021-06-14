'''
- write and then data reading.
- W+ method is work First data write and after data read.
'''

f = open('write+method', 'w+')
# Eries before data form inside File.
f.write('My Name Is Tejas')

data = f.read()
# output become a blank. because after writing cursor is last position and last position to start read.
print(data)

# so read your file than used seek method and cursor position is reset to 0. and then read data
f.seek(0)
data1 = f.read()
print(data1)
