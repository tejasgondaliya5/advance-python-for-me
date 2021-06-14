# take input from user Tuple Format(%s, %s, %s)..........................

import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection ....... successfully')
except:
    print('connection ........ denied')
sql = 'insert into student(stu_name, stu_roll, fees) values(%s, %s, %s)'
myc = conn.cursor()

name = input('Enter Student name :- ')
roll = int(input('Enter you roll :- '))
fees = float(input('Enter your Fees :- '))

peram = (name, roll, fees)

try:
    myc.execute(sql, peram)
    conn.commit()
except:
    conn.rollback()
    print('insertion denied')

myc.close()
conn.close()