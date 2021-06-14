# take input from user Dictionary Format(%(key)s, %(key)s, %(key)s)..........................

import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection ....... successfully')
except:
    print('connection ........ denied')
sql = 'insert into student(stu_name, stu_roll, fees) values(%(n)s, %(r)s, %(f)s)'

myc = conn.cursor()
name = input('Enter Student name :- ')
roll = int(input('Enter you roll :- '))
fees = float(input('Enter your Fees :- '))
peram = {'n': name, 'r': roll, 'f': fees}
try:
    myc.execute(sql, peram)
    conn.commit()
except:
    conn.rollback()
    print('insertion denied')

myc.close()
conn.close()