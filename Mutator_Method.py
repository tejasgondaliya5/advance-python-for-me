'''
--> Mutator method / setter method
- Mutator method is one type of instance method
- Mutator method is also called set method
- Mutator method is used to access or read,write and modification
- Mutator method is syntex of progarm EX : def set_value(self):
                                           def set_result(self):
                                           def set_name(self):
                                           def set_id(self):

'''
class Surname:
    def __init__(self):
        self.fname = "Tejas"

    def set_name(self):     # complsary method name is start set_method name
        self.fname = "raj"  # Access or read,write and modification data

obj = Surname()
print(obj.fname)

obj.set_name()
print(obj.fname)