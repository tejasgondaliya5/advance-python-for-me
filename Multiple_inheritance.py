'''
- Multiple inheritance no matalab ke koi ek child class na 1 thi vadhare parent class hoy to tene Multiple inheritance kehavay 6.
- EX:-  --> class Father:                # parent class

        --> class Mother:                # parent class

        --> class Son(Father, Mother):   # child class
'''

class Father:
    def __init__(self):
        super().__init__()
        print("Father class ka constructor")

    def ShowF(self):
        print("Father class ka method")

class Mother:
    def __init__(self):
        super().__init__()
        print("Mother class ka constructor")

    def ShowM(self):
        print("Mother class ka method")

class Son(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Son class ka constructor")

    def ShowS(self):
        print("Son class ka Method")

obj = Son()
''' ama costructor call thoduk tripical 6. 

--> First son calss no object creat thay.
--> pachi tema super().__init__() malavathi te tena first parent class Father class na constructor ma jay.
--> pachi tema super().__init__() malvathi te tena parent object class ma jay.
--> object class no koi constructor na hova thi te mother class na constructor ma jay.
--> tema super().__init__() male pan tena parent class ne ek vakhat call thayo hovathi biji vakhat call na thay.
--> etle pela mother class no constructor print thay, pachi father class no constructor print thay, pachi son class no constructor print thay.

1) son class no constructor
2) father class no constructor
3) object class ma constructor na hova thi mother class no constructor call thay
4) mother class no const.. print thay
5) father class no const.. print thay
6) son class no const.. print thay
'''
print()

obj.ShowS()
obj.ShowM()
obj.ShowF()