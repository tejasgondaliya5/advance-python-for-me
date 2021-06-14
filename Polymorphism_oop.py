'''
- Poly : many,
- morphism : forms
--> types of Polymorphism :-
      1) Duck Typing
      2) Operator Overloading
      3) Method Overloading
      4) Method overriding
'''

# ......... 1) Duck Typing ...........
''' Duck typing is call method inside function '''

class Duck:
    def walk(self):
        print("thapk thapk thapk thapk")

class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")

class Cat:
    def talk(self):
        print("Meow Meow")

# this is Duck typing Function
def printFunction(obj):         # that is function but inside call object that is Duck Typing
    obj.walk()                  # that is no meter which type method that work only call object.methodname


d = Duck()
printFunction(d)

h = Horse()
printFunction(h)

# c = Cat()
# printFunction(c)   # this function is given Error becuse printfunction is only object.walk() run but this is object.talk()