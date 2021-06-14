# finally exception is run always. with exception and without exception

a = 10
b = 5

try:
    c = a/b
    print(c)

except ZeroDivisionError:
    print('zero divide by is not allow')

finally:
    print('finally inside is run successfully')

print('rest of the code')

print()
print('..............................................')
print()


a = 10
b = 0

try:
    c = a/b
    print(c)

except ZeroDivisionError:
    print('zero divide by is not allow')

finally:
    print('finally inside is run successfully')

print('rest of the code')