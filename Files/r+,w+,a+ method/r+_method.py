# Read then write

# read+ method is first read and after write.
# means aa apend jevu kam kare for EX:- suppose file ma 'hello tejas' lakhelu 6.
# pachi tame r+ method thi first data read thay pachi data write thay
f = open('read+mode.txt', 'r+')

data = f.read()                 # First read method call so work.

f.write('my name is tejas\n')   # after write method


print(data)
print(f.tell())



# jo tame pela data write kara vo to progarm thi write na thay.
# and old data corrupt thai jay.

# f = open('read+mode.txt', 'r+')
#
# f.write('my name is tejas\n')   # first Write method run so  gadbad
#
# data = f.read()                 # after read method so gadbad
# print(data)
# print(f.tell())