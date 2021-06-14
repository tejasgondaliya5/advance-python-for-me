#........ operator overloding ..............
# print(10+20)  # how work +(add)

# print(int.__add__(10, 20))
# print(int.__sub__(20, 10))
# print(int.__mul__(10, 20))
# print(int.__divmod__(20, 3))

# print()
# print(str.__add__("tejas", "Gondaliya"))

class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return  self.x + other.y

class B:
    def __init__(self, y):
        self.y = y

a = A(1000)
b = B(2000)
print(a+b)
