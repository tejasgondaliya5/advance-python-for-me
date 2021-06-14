f1 = open('openFile.txt', 'r')    # which file copy that file is open read mode
f2 = open('copy_File.txt', 'w')   # and after open second file that file open in writen mode.

data = f1.read()
print(data)

f2.write(data)

f1.close()
f2.close()