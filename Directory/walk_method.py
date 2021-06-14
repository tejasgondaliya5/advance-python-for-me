import os
w = os.walk('.')    # . ni jagya e directory no path pan api sko  EX:- os.walk('D:\pycharm\\advancpython')
for i in w:
    print(i)
print()

w = os.walk('.', topdown=False)
for i in w:
    print(i)