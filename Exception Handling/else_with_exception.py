# this program run try and else:

a = 10
b = 5

try:
    c = a/b
    print(c)

except ZeroDivisionError:
    print('zero divide by is not allow')

else:
    print('program is run successfully')


print()
print('..............................................')
print()


# this program is run except not try or else

a = 10
b = 0

try:
    c = a/b
    print(c)

except ZeroDivisionError:
    print('zero divide by is not allow')

else:
    print('inside else program is run successfully')
