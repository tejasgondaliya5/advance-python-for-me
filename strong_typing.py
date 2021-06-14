'''
- whay use strong typiong :- agar hame specify karna he ke Duck Typing ma je Function object thi method call kartu hatu te
  method te object vala class ma 6 ke nahi.
-
'''

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
def printFunction(obj):
    if hasattr(obj, 'walk'):
        obj.walk()
    if hasattr(obj, "talk"):
        obj.talk()

d = Duck()
printFunction(d)

h = Horse()
printFunction(h)

c = Cat()
printFunction(c)    # this line ERROR is solve