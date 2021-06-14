'''
a) Lock
b) RLock
c) Semaphore

--> a) Locks:-
         1) acquire() :-
                        acquire() jya lagavi e tya Lock gali jay and jay sudhi release na karo tya sudhi tema lock reyu.
                        Syntax:- acquire(blocking = True, timeout = -1)
         2) release():-
                        release() method no used lock ne release karva mate thay 6.
                        Syntax:- release()
'''

from threading import Thread, currentThread, Lock

class Flight:
    def __init__(self, Available_seat):
        self.Available_seat = Available_seat
        self.l = Lock()                                   # decler Lock variable in used method

    def resreve(self, Need_seat):
        self.l.acquire()                                   # this is acquire(Lock) Method call
        print("available seat is :", self.Available_seat)
        if (self.Available_seat >= Need_seat):
            name = currentThread().getName()
            print(f"{Need_seat} seat is alloted for {name}")
            self.Available_seat -= Need_seat
            print("available seat is :", self.Available_seat)
            print()


        else:
            print("sorry! All seat has alloted")
        self.l.release()                                          # release Lock from lock Thread

f = Flight(5)
t1 = Thread(target=f.resreve, args=(1,), name="Tejas")    # name= "tejas"   means   setName = "tejas"
t2 = Thread(target=f.resreve, args=(1,), name="raj")
t3 = Thread(target=f.resreve, args=(1,), name="ravi")
t4 = Thread(target=f.resreve, args=(1,), name="harsh")
t5 = Thread(target=f.resreve, args=(1,), name="jay")
t6 = Thread(target=f.resreve, args=(1,), name="kuldip")
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()