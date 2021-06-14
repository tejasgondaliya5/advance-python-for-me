'''
- Daemon Thread Continues Which Run Continuously in the Background.
- IMP:- It Provides Support to non-daemon thread.
- When last Non-daemon thread terminates, Automatically all daemon thread will be terminated.

--> create daemon Thread:-
      - setDaemon(True) Method
               or
      - daemon = True Property is used

--> EX:-  t1 = Thread(target=disp)
          t1.setDaemon(True)         #  Made non-daemon thread to daemon Thread
          t1.setDaemon(False)        #  Made non-daemon thread
               or
          t1.daemon = True           # another trick to create non-daemon thread to daemon Thread
          t1.daemon = False          # Made non-daemon thread

- interview Q. :- Main Thread is Daemon thread or non-daemon thread
       --> Ans :- non-daemon thread

'''

from threading import Thread, currentThread


def disp():
    print("Disp Thread")


t1 = Thread(target=disp)
print("Before set daemon : ", t1.isDaemon())
t1.setDaemon(True)
# t1.daemon = True                               # aa rite pan declare thay daemon thread
print("After set demon : ", t1.isDaemon())

t1.start()                      # start thread after  declare daemon thread

print()


#.......................................................................................

def disp():
    print("disp Function")

mt = currentThread()
print(mt.getName())
print(mt.isDaemon())

t1 = Thread(target=disp())

print(t1.isDaemon())
t1.start()