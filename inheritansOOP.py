# inheritance concepet of oop
'''
-inheritance is concept of parent and child relation
- inheritance meaans new class deriving a old class

- 1)super class : old class is called super class, parent class, base class
- 2)sub class : new class is called sub class, child class, derived class

- type of inheritance :
  1) Single inheritance
  2) Multi level inheritance
  3) Hierarchical inheritance
  4) Multiple inheritance
'''

# ....... 1)Single inheritance ..........

class Father:
    house = "4bhk"

    def __init__(self):
        self.car = "BMW"
        self.money = "10cr"

    def show(self):
        print("this is Father class : ")
        print("father car is :", self.car)
        print("father money :", self.money)
        print("father house is :", obj.house)

class Child(Father):
    def disp(self):
        self.buisness = "software compney"

        print("this is child class :")
        print("child buisness is :", self.buisness)


obj = Child()
obj.disp()

print()
obj.show()