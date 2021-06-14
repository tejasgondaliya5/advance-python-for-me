'''
Theread:-
  - Thread is a separate flow of execution. Every thread has a task.

Multithreading:-
  - multithreading is more thane one thread.
  - EX:- Union bank app |--------->  tejas access union bank app
                        |
                        |--------->  Bansi access union bank app
                        |
                        |--------->  Raj access union bank app
'''

'''
Main Thread:-
  - Main thread is created automatically when your program is started.
  - EX:- give below small code
'''
import threading

print("Tejas Gondaliya")
t = threading.currentThread().getName()

print(t)