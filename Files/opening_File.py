'''
- open :- If we want to use a file or its data, first we have to open it.
      - Syntax:- open('filename', mode='r', buffrering, encoding=None,errors=None, newline=None, closefd=True, opener=None)
          - EX:- f1 = open('student.txt', mode='w,r,rb,a')

encoding = None or uft-8
'''

f = open('student.txt', 'r')
print(f)
data = f.read()
print(data)
f.close()

f = open('student.txt')    # 'r' is by defult work.
print(f)
data = f.read()
print(data)
f.close()
