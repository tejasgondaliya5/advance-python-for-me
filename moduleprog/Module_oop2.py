import First
import Second

print(First.a)
First.name()
print()

print(Second.a)
Second.name()
print()

from First import a as A, name as n
from Second import a, name

print(A)
print(a)
