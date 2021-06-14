'''

constructor is automatic call.
jetla object bane etlivar constructor call thay.

'''


# class Mobile:
#     def __init__(self):
#         print("mobile constructor called")      # without call constructor, constructor can called automatically
# o1 = Mobile()
# print()

# constructor with argument
class Fun:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printdetail(self):
        age = 20
        print("constructor name is :", self.fname, self.lname)
        print("age is :", age)

obj = Fun("Tejas", "Gondaliya")
obj.printdetail()
print("id is :", id(obj))