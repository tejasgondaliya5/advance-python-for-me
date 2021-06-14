'''
- jyare parent class and child class bane ma constructor banavo
  tyare parent class no constructor work na kare because this situation
  is constructor overriding.

- How to solve this situation :-
     --> super() :- super() ka use kar ke  constructor overrding
                    ko solve kari saki ye

'''

class Father:
    def __init__(self,m):
        self.money = m
        print("parent class constructor")

    def show(self):
        print("parent class instance method")

class Son(Father):
    def __init__(self, m, j):
        super().__init__(m)
        self.job = j
        print("Son class constructor")

    def disp(self):
        print("son class instance method", self.money)
        print("your job is :", self.job)

obj = Son(1000, "python")
obj.disp()