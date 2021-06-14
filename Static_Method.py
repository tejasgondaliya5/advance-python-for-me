'''
Static method is
'''

class Name:
    fname = "Tejas"

    @staticmethod
    def printdetail(lname):
        print("my name is :", Name.fname, lname)

obj = Name()
Name.printdetail("Gondaliya")
obj.printdetail("patel")
