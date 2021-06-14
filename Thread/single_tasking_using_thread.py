from threading import Thread
from time import sleep
class MyThread:
    def solve_question(self):
        self.q1()
        self.q2()
        self.q3()

    def q1(self):
        sleep(3)
        print("question 1 solve.")
        sleep(3)

    def q2(self):
        print("question 2 solve.")
        sleep(3)

    def q3(self):
        print("question 3 solve.")


obj = MyThread()

t = Thread(obj.solve_question())
