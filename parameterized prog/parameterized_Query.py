'''
%s :- is used as format style in the sql Queries, while using tuple parameters.
%(key) :- is used as a format style in  the sql queries, while using dictionary parameters.
'''

import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection ....... successfully')
except:
    print('connection ........ denied')
sql = 'insert into student(stu_name, stu_roll, fees) values(%s, %s, %s)'
myc = conn.cursor()
peram = ("mayur", 106, 27560)
try:
    myc.execute(sql, peram)
    conn.commit()
except:
    conn.rollback()
    print('insertion denied')

myc.close()
conn.close()