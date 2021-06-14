'''
- Thread creating without using class.
    --> SYNTEXT:- thread_object = Thread(target = function_name, args = (arg1,arg2,...))
- creating a thread by creating a child class to thread class.
'''

# Thread creating without using class.

from threading import Thread

def disp(a,b):
    print("thread with argument.", a, b)

def show():
    print("Thread without argument")

t = Thread(target=disp, args=(10,20))
t1 = Thread(disp(10,20))

 
t.start()

t1.start()
print()

for i in range(5):
    s1 = Thread(show())

