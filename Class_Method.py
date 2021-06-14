'''
- class method is used to access calss variable inside class
- class method is used to decorate "@classmethod"
- class method is call out side class "class_name.method_name(argument)"
'''

class Surname:
    fname = "Tejas"

    @classmethod          # this is classmethod decorator
    def name(cls):        # this is class method
        print("name is :", cls.fname)

obj = Surname()
Surname.name()   # call class method "class_name.method_name()"