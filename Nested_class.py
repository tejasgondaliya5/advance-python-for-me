class School:
    # outer class constructor
    def __init__(self):
        self.sname = "Dharti vidhaya vihar"
        # create inner class object create
        self.obj1 = self.Teacher()

    # outer class method
    def show(self):
        print("school name is :", self.sname)

    # create inner class
    class Teacher:
        # inner class constructor
        def __init__(self):
            self.tname = "kajal patel"
            self.tsub = "science"
            self.tstd = "7th"

        # inner class method
        def disp(self):
            print("teacher name is :", self.tname)
            print("teacher subject is :", self.tsub)
            print("teacher which standerd teach :", self.tstd)

# create outer class object
obj = School()

# create inner class object out side class  # ....aa rite pan banvi sakay....
'''obj2 = School().Teacher()'''

# call outer class method
print()
obj.show()
print(obj.sname)

# call inner class method
print()
obj.obj1.disp()
print(obj.obj1.tname)
print(obj.obj1.tsub)

# second trick to writen object in inner class
print()
obj2 = obj.obj1
obj2.disp()
print(obj2.tname)
print(obj2.tsub)
