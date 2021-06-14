'''
- Create Thread class with Class.
'''

from threading import Thread


class Father(Thread):
    def run(self):
        for i in range(5):
            print("Child Thread")


class Son(Thread):
    def disp(self):
        for i in range(5):
            print("second Child Thread")


F = Father()
F.start()
F.join()  # join method is run child method it can not run any method

S = Son()                  # aa rite call pan thay
t = Thread(target=S.disp())   # and aa rite pan call thay
t.start()

for i in range(5):
    print("Main Thread")

'''
NOTE:- ama output join method used karie teni agal nu thread line ma print thay.
       pachi pachal na badha line ma na ave.
'''
