from threading import Thread

class Mythread:
    def disp(self):
        print("child Thread")

m = Mythread()
to = Thread(target=m.disp)
to.start()
print()

t1 = Thread(m.disp())
t1.start()