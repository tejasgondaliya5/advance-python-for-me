'''
- Method overloding concept is does not work in python.
- But Method ovrloding in diffrent types.
- EX:- koi ek method ma different different task perform thay tene method overloading kehvay 6.
'''

class Math:
    # def Sum(self, a, b, c):
    def Sum(self, a = None, b=None, c=None):   #  this one method but perform differnt task that reason this is method overloading
        if a!=None and b!=None and c!=None:
            s = a+b+c

        elif a!=None and b!=None:
            s = a=b

        else:
            s = "Provide minimum two argument"

        return s

obj = Math()
print(obj.Sum(10, 20, 30))
print(obj.Sum(10, 20))
print(obj.Sum(10))