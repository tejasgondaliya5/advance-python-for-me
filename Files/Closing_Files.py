'''
- Close File - close() --> this method is used to close, open file.
- once we closed the file, file objects is detected form the memory hence file file will be no longer accessible unless we open it again.
- if you don,t explicitly close a file, python,s garbage collector will eventually destroy the object and close the open file for you, but the file
  may stay open for a while so you should always close opened file.

'''
f1 = open('student.txt')

f2 = open('student1.txt')

f1.close()

f2.close()