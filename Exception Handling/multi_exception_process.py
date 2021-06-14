a = 10
b = 0

try:
    c = a/b
    print(c)

except ZeroDivisionError as ex:
    print(ex)

print('rest of the code')


print()
print('...............................................')
print()


a = 10
b = 0

try:

    d = a/g      # g is not defined  so g is name error
    print(d)

except ZeroDivisionError as ex:
    print(ex)

except NameError as na:
    print(na)

print('rest of the code')