# Module ma apde Python ni file ne mange karva ni hoy.
'''
     second program Modules_oop2 ma 6.
- 1) import module name
- 2) import module name  as alias name
- 3) from module name import function name
- 4) from module name import f name as alias name
- 5) from module name import*

'''
# 1)....... impot module name .........

import Main
print(Main.a)
Main.add(10, 20)

Main.sub(20, 10)
print()

sum = Main.add
sum(10, 20)
print()

# 2).......import module name as alias name........

import Main as M
M.add(10, 20)

M.sub(20, 10)

print()

# 3)....... from module name import function name ........

from Main import a, add, name
print(a)
add(10, 20)
name()

print()

# 4) ........ from module name import f name as alias name .......

from  Main import  add as M, sub as s

M(10, 20)

s(20, 10)
print()

# 5) ........ from module name import* .......

from Main import *

print(a)
name()
add(10, 20)