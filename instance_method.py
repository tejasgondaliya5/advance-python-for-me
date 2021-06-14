'''
- instance method ma instance variable no use thay
-> two type of instance method :
       1) Accessor method
       2) Mutator method
'''

class Fun:
    def __init__(self):
        self.fname = "tejas"  # this is instance variabe

    def inst_methos(self, lname):    # this is instance method
        self.lname = lname
        print("name is :", self.fname, self.lname)  # this is access instance variable

obj = Fun()
obj.inst_methos("Gondaliya")  # calling instance method
