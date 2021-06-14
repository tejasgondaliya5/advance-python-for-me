'''
- Hierarchical inheritance ma ek parent ek thi vadhare child hoy tene hierarchical
  inheritance kehvay
- EX:- class Father:
       class son(Father):
       class Dauhter(Father):
'''
class Father:
    def __init__(self):
        print("father class ka Constructor")

    def ShowF(self):
        print("Father class ka Method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son class ka Constructor")

    def ShowS(self):
        print("Son class ka Method")

class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Daughter class ka Constructor")

    def ShowD(self):
        print("Daughter class ka Method")

Sobj = Son()        # son class ka object
print()

Dobj = Daughter()   # Daughter class ka method
print()

Sobj.ShowS()     # son class ka object access son class method
Sobj.ShowF()     # son class ka object access Father class method
print()

Dobj.ShowD()    # Daughter class ka object access Daughter class method
Dobj.ShowF()    # Daughter class ka object access Father class method