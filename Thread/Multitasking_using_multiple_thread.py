'''
two task using two thread
'''
from threading import Thread

class Hotel:
    def __init__(self, t):
        self.t = t

    def food(self):
        for i in range(5):
            print(self.t, i)


h1 = Hotel("Take order From Table :")
h2 = Hotel("serve order to table :")

t1 = Thread(target=h1.food)
t2 = Thread(target=h2.food)

t1.start()
t2.start()