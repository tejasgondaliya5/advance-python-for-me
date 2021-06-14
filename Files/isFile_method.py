import os
# print(os.path.isfile('student.txt'))

if os.path.isfile('ironhart.txt'):
    f1 = open('ironhart.txt')
    print("file is open")
    f1.close()
else:
    print("file is not Found")