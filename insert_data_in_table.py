'''
commit() Method:- commit() method no used kari ne apde je kai pan table ma change kari e te save thai jay.
                - jo commit() method no used na kri e to table na changes karie te save na thay.

                - commit() method AUTO complete nathi mate tene command thi access kari sakay.

rollback() Method:- jo connection ma koi ERROR ave to te ERROR ne rollback kare.
                  - EX:- koi website ke application ma payment transaction thatu hoi ane Internet Connection lose thay to
                         te payment ne roll back kari dey.(matlab ke apde fari thi badhi detail fill kari pade).
'''

import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection....... successfully')
except:
    print('connection...... denied')

sql = 'insert into student(stu_name, stu_roll, fees) VALUES("Tejas", 101, 10000.52), ("raj", 102, 105220.24)'
myc = conn.cursor()
myc.execute(sql)
try:
    conn.commit()
    print('save to data in databases')
except:
    conn.rollback()                    # rollback tyare use thase jayare commit bai thay.
    print('unable to insert data')
myc.close()
conn.close()

