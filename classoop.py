# Class is a group of attributes and methods.
'''

- Attributes : Attributes are represented by variable

- Method : Method is represented by Function (99% same)

- __init__() : this is constructor and this is used only initialize the variable. and aa method ne
               call karvani jarur nathi padti.

- self : self ni pase current class na object hoy

'''

class Fun:
    def __init__(self, age):
        self.age = age
        self.fname = "tejas"
        self.lname = "Gondaliya"

    def printdetail(self,ccity):
        city = ccity
        print("first name is :", self.fname,self.lname)
        print("age is :",self.age)
        print("city is :", ccity)

f1 = Fun(21)
# f2 = Fun(20)
f1.printdetail("ahmedabad")
# f2.printdetail("surat")

print(f1.fname)
# f1.fname = "bansi"
