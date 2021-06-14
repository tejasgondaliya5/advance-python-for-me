# ............................... Without using Daemon Thread ...............................

# from threading import Thread, currentThread
# from time import sleep
#
# def Teaching():
#     for i in range(1,11):
#         print("Teaching Seassion :", i)
#         sleep(1)
#
# t1 = Thread(target=Teaching)
# t1.start()
# sleep(6)
# print("Exam Finish", currentThread().getName())


# ..................................... using Daemon Thread .....................................

from threading import Thread, currentThread
from time import sleep


def Teaching():
    for i in range(1, 11):
        print("Teaching Seassion :", i)
        sleep(1)


t1 = Thread(target=Teaching)
t1.setDaemon(True)
t1.start()
sleep(6)
print("Exam Finish", currentThread().getName())
