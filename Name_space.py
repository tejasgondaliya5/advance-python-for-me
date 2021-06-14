'''
- Name space ma etluj ave ke jo koi class variable hoy tene class_name.variable_name ne modify
  kare to class variable name and badha object variable name change thay
- pan jayre koi specific object through variable name change karo to te khali te variable ni
  andar j change thay bija object ma teno koi fark na pade
'''

class Fun:
    fname = "Tejas"

    @classmethod
    def cls_variable(cls):
        print(cls.fname)

print("fname =", Fun.fname)

obj = Fun()
obj1 = Fun()
print()

# .....change fname value through object variable.....
print("chnge only object though variable name : ")
obj.fname = "raj"
print("obj = ", obj.fname)     # change only this object value
print("obj1 = ", obj1.fname)    # not change this object value
print("Fun = ", Fun.fname)
print()

# .....change fname value through class variable.....
print("change class through variable name : ")
Fun.fname = "raj"    # change class through change variable name
print("Fun = ", Fun.fname)     # change class varible value
print("obj = ", obj.fname)     # cahnge object variable value
print("obj1 = ", obj1.fname)

