f1 = open('student.txt')
print("File Name:-", f1.name)
print("File mode:-", f1.mode)
print("File encoding:-", f1.encoding)
print("File readable:-", f1.readable())
print("File writable:-", f1.writable())
print("File closed:-", f1.closed)
print()

print('*********************************************')

print()
f1 = open('student.txt', 'w')
print("File Name:-", f1.name)
print("File mode:-", f1.mode)
print("File encoding:-", f1.encoding)
print("File readable:-", f1.readable())
print("File writable:-", f1.writable())
print("File closed:-", f1.closed)
print()

print('*********************************************')

print()
f1 = open('student.txt', 'a')
print("File Name:-", f1.name)
print("File mode:-", f1.mode)
print("File encoding:-", f1.encoding)
print("File readable:-", f1.readable())
print("File writable:-", f1.writable())
print("File closed:-", f1.closed)
print()

print('*********************************************')

print()
f1 = open('student.txt', 'r+')
print("File Name:-", f1.name)
print("File mode:-", f1.mode)
print("File encoding:-", f1.encoding)
print("File readable:-", f1.readable())
print("File writable:-", f1.writable())
print("File closed:-", f1.closed)
print()

print('*********************************************')

print()
f1 = open('student.txt', 'w+')
print("File Name:-", f1.name)
print("File mode:-", f1.mode)
print("File encoding:-", f1.encoding)
print("File readable:-", f1.readable())
print("File writable:-", f1.writable())
print("File closed:-", f1.closed)
print()

print('*********************************************')

print()
f1 = open('student.txt', 'a+')
print("File Name:-", f1.name)
print("File mode:-", f1.mode)
print("File encoding:-", f1.encoding)
print("File readable:-", f1.readable())
print("File writable:-", f1.writable())
print("File closed:-", f1.closed)
print()

print('*********************************************')

print()
f1 = open('tejas.jpeg', 'rb')
print("File Name:-", f1.name)
print("File mode:-", f1.mode)
# print("File encoding:-", f1.encoding)                   # binary file Encode na thay
print("File readable:-", f1.readable())
print("File writable:-", f1.writable())
print("File closed:-", f1.closed)
print()

print('*********************************************')

print()
f1 = open('tejas.jpeg', 'wb')
print("File Name:-", f1.name)
print("File mode:-", f1.mode)
# print("File encoding:-", f1.encoding)                   # binary file Encode na thay
print("File readable:-", f1.readable())
print("File writable:-", f1.writable())
print("File closed:-", f1.closed)
print()

print('*********************************************')

print()
f1 = open('tejas.jpeg', 'rb+')
print("File Name:-", f1.name)
print("File mode:-", f1.mode)
# print("File encoding:-", f1.encoding)                   # binary file Encode na thay
print("File readable:-", f1.readable())
print("File writable:-", f1.writable())
print("File closed:-", f1.closed)
print()

print('*********************************************')

print()
f1 = open('tejas.jpeg', 'wb+')                            # wb+ is bugged because file is open readable mode 
print("File Name:-", f1.name)
print("File mode:-", f1.mode)
# print("File encoding:-", f1.encoding)                   # binary file Encode na thay
print("File readable:-", f1.readable())
print("File writable:-", f1.writable())
print("File closed:-", f1.closed)
print()