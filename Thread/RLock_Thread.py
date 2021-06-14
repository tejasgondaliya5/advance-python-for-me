from threading import Thread, currentThread, Lock, RLock

class Flight:
    def __init__(self, Available_seat):
        self.Available_seat = Available_seat
        self.l = RLock()                                # decler Lock variable in used method
        print(self.l)

    def resreve(self, Need_seat):
        self.l.acquire()                                   # multiple time acquire(Lock) Method call
        self.l.acquire()
        print(self.l)
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
        self.l.release()                                          # release Lock from lock Thread
        print(self.l)


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