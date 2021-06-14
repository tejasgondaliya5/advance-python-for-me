'''
- File is the collection of data that is available to a program.
- We can retrieved and use data Store in a file Whenever we required.

--> Advantages :-
    - Stored data is permanent unless someone remove it.
    - stored data can be shared.
    - it is possible to update or remove the data.

- There are two type of files:-
     - Text File :-
              It Store data in the form of character. it is used to store characters and strings.
     - Binary File :-
              It Stored data in the form of bytes, a group of 8 bit each. It is used to store text, images, pdf, csv,
              video and audio.
'''

f = open('student.txt', mode='w')        # 'w' means Written mode open.
f.write('my name is tejas')
f.close()

f = open('student.txt', mode='r')        # 'r' means Read mode open.
print(f.read())
f.close()