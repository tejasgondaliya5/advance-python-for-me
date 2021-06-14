class Selfdetail:

    fname = "tejas"          # this is class variable

    def __init__(self):
        self.lname = "Gondaliya"


    def printdetail(self):
        print("name is :", obj.fname, self.lname)        # access class variable without decorator


    @classmethod              # access class variable with decorator
    def show(cls):
        print(cls.fname)



obj = Selfdetail()
obj.printdetail()

Selfdetail.show()            # access calss variable outside class with decorator

print(Selfdetail.fname)          # Access class variable outside only class_name.variable_name