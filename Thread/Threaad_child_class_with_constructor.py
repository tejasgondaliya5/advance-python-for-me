from threading import Thread

class Mythread(Thread):
    def __init__(self, a):
        Thread.__init__(self)
        print("child Thread constructor", a)

    def run(self):
        pass

m = Mythread(10)
m.start()

print("Main Thread")
