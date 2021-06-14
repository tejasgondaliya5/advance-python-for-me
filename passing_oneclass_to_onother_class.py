class Student:
    def __init__(self, fname, rollno):
        self.fname = fname
        self.rollno = rollno

    def disp(self):
        print("student name is :", self.fname)
        print("student roll no is :", self.rollno)

class User:

    # create static maethod
    @staticmethod
    def Show(s):
        print("user name is :", s.fname)
        print("user roll no is :", s.rollno)
        s.disp()


# object for student class
obj = Student("Tejas", 19)

# static method call with Student calss object
User.Show(obj)