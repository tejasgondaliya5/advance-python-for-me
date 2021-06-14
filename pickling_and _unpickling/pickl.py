# pickling method
import pickle, pickling_and_unpickling as cl

n = int(input("Enter Number of student : "))
with open('pickling_File.txt', 'wb') as f:
    for i in range(n):
        name = input('Enter student name :')
        roll = int(input('enter studebt roll number : '))
        address = input('Enter city name :')

        stu1 = cl.Student(name, roll, address)
        pickle.dump(stu1, f)