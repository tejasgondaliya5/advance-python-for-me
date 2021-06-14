'''
************* Race Condition ********************
- Race condition means unexpected output that program.
- what is advantages for using Thread creat flight booking api
   --> 1) first badha user mate sepreat thread creat thay
   --> 2) second je pela access thay te pela tickit book thay
   --> 3) EX:- program nu output darkhele change thay but ghani var output unexpected ave.
               tene race condition kehvay

************ solve race condition *******************
'''
from threading import Thread, currentThread

class Flight:
    def __init__(self, Available_seat):
        self.Available_seat = Available_seat

    def resreve(self, Need_seat):
        print("available seat is :", self.Available_seat)
        if (self.Available_seat >= Need_seat):
            name = currentThread().getName()
            print(f"{Need_seat} seat is alloted for {name}")
            self.Available_seat -= Need_seat
            print("available seat is :", self.Available_seat)
            print()

        else:
            print("sorry! All seat has alloted")

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