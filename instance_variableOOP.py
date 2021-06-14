class Instanc_variable:
    def __init__(self):
        self.fname = "tejas"        # Self.fname is instance variable
        self.lname = "Gondaliya"    # Every variable under the constructor that is instance variable

    def printdetail(self):          # that is instance method
        print("inside class access instance_variable :",self.fname, self.lname)  #instance variable used under calss that use keyword self.variable_name

obj = Instanc_variable()
print("out side the class instance_variable : ",obj.fname,obj.lname)     # instance variable usedc out of the class  that use object_name.variable_name

obj.printdetail()
