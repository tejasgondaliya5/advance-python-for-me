'''
- why use method overriding :- because parent class method behavior change in child class that case is method overriding
- use parent class method using to super() method.
'''

class Add:
    def Show(self, x, y):
        print("Addition :", x+y)

class Sum(Add):
    def Show(self, a, b):                 # this is method overriding because Show() method is parent class and child class
        super().Show(20, 30)              # this is super method
        print("Multiplication :", a*b)

obj = Sum()
obj.Show(10, 20)
