'''
- Event Method:-
'''

from threading import Thread, Event
from time import sleep

def light_swtch():
    sleep(3)
    e.set()
    print('Green Light ON')
    sleep(5)
    print('Red light ON')
    e.clear()
def traffic():
    e.wait()
    while e.is_set():
        print("you can go.......")
        sleep(0.5)

    print('program Done')

e = Event()
t1 = Thread(target=light_swtch)
t2 = Thread(target=traffic)

t1.start()
t2.start()
