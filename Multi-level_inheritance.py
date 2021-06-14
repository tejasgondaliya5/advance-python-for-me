'''
- multi level inheritance ma parent class mathi child class derived thay
  pachi te child class mathi tena pan child class derived thay it's called
  multi level inheritance

- EX:- --> class Father:

       --> class Son(Father):

       --> class Grandson(Son):

'''
class Father:
    def __init__(self):
        super().__init__()
        print("father constructor")

    def shoef(self):
        print("father class method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("son constructor")

    def shows(self):
        print("son class method")

class Grandson(Son):
    def __init__(self):
        super().__init__()
        print("grandson constructor")

    def showg(self):
        print("grandson class method")

obj = Grandson()
print()

obj.showg()
obj.shows()
obj.shoef()
