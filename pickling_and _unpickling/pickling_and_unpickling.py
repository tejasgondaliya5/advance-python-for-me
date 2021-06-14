'''
- Pickling and unpickling method is used to stored your data with organized structure.
- Pickling EX:-    stu1 object and stu2 object is stored in file using dump() method that is pickling.
- unpickling EX:-  then read data in File using load() method that is unpickling.
'''

import pickle

class Student:
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self.addess = address

    def disp(self):
        print(f'name : {self.name}, roll is : {self.roll}, address : {self.addess}')

# shapret pickling method used to input from user program is pickl.py program
# # pickling method
# with open('pickling_File.txt', 'wb') as f:       # open always write binary mode
#     stu1 = Student('Tejas', '101', 'Ahmedabad ')  # create stu1 object from class
#     stu2 = Student('Raj', '102', 'Bagasra')      # create stu2 object from class
#     pickle.dump(stu1, f)                         # using dump() method data store in file from binary mode
#     pickle.dump(stu2, f)                         # using dump() method data store in file from binary mode
#


# shapret unpickling method used to input from user program is unpickl.py program
# # unpickling method
# with open('pickling_File.txt', 'rb') as f:      # open always read binary mode
#     data1 = pickle.load(f)                       # using load() method read data from file.
#     data2 = pickle.load(f)                       # using load() method read data from file.
#     data1.disp()                                 # and print data from read data.
#     data2.disp()                                 # and print data from read data.