import First
import Second

obj = First.Myclass()
obj.name()

obj1 = First.Myschool()
obj1.show()
print()

sobj = Second.Mycollege()
sobj.disp()

sobj1 = Second.Myschool()
sobj1.show()


print('.....................................................')

# **********************************************************

import First as f
import Second as s

obj = f.Myclass()
obj.name()

obj1 = f.Myschool()
obj1.show()
print()

sobj = s.Mycollege()
sobj.disp()

sobj1 = s.Myschool()
sobj1.show()

print('.....................................................')

# # **********************************************************

from First import Myclass, Myschool
from  Second import Mycollege, Myschool

obj = Myclass()
obj.name()

obj1 = Myschool()
obj1.show()     # this line is call by second class because First module and Second module same class
print()

sobj = Mycollege()
sobj.disp()

sobj1 = Myschool()
sobj1.show()

print('.....................................................')

# **********************************************************
from First import *
from Second import *

obj = Myclass()
obj.name()

obj1 = Myschool()
obj1.show()        # this line is call by second class because First module and Second module same class
print()

sobj = Second.Mycollege()
sobj.disp()

sobj1 = Second.Myschool()
sobj1.show()

