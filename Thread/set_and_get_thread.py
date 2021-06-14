'''
- getName :- given thread name
- setName :- set thread name

'''

from threading import Thread, currentThread

def disp():
    print("Child Thread object", currentThread().getName())      # display show Thread name
    currentThread().setName("Doc Thread")                        # change Thread name   __setName__
    print("Child Thread object", currentThread().getName())      # display change thread name


t =Thread(target=disp)          # define Thread 1
t2 =Thread(target=disp)          # define Thread 2

print()
t.start()                       # start Thread 1
t2.start()                      # start Thread 2

print()
print("Main Thread", currentThread().getName())               # display show Thread name
currentThread().setName("personal Thread")                    # change Thread name
print("Main Thread", currentThread().getName())               # display change thread name

print()
print("defult name ", t.getName())             # get Thread name out of the Thread
t.setName("tejas Thread")                      # change Thread name
print("after set name ", t.getName())          # display change thread name out of the Thread


''' NOTE :- output ma Execution naki na hoy game tyare game te thay.
            Mate output darkhele alag hoy.'''