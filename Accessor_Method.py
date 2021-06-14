'''
--> Accessor method / getter method
- Accessor method is one type of instance method.
- Accessor method is also called get method.
- Accessor method is used to access or read the data.
- Accessor method is syntex of program EX : def get_value(self):
                                            def get_result(self):
                                            def get_name(self):
                                            def get_id(self):
'''

class Surname:
    def __init__(self):
        self.fname = "Tejas"

    def get_Name(self):     # complsary method name is start get_method name
        return f"name is : {self.fname}"    # only access or read data

obj = Surname()
a = obj.get_Name()
print(a)