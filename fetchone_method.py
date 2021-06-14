# commit() method used can not mandatory.
# because fetchone method used to only fetch data not change in table.

import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123',host='localhost', database='student', port=3306)
    print('connection....... successfully')

except:
    print('connection.......... filed')

myc = conn.cursor()

try:
    myc.execute( 'select * from student' )
    row = myc.fetchone()
    while row is not None:
        # print(row)        # aa rite print karva thi output tuples na form ma male. je saru na lage.
                            # mate niche parmane apde print karyu 6.
        stuid = row[0]
        stu_name = row[1]
        stu_roll = row[2]
        fees = row[3]
        print(f'student ID : {stuid} , stu_name : {stu_name} , stu_roll : {stu_roll} , fees = {fees}')
        row = myc.fetchone()
    print('total rows:', myc.rowcount)

except:
    conn.rollback()
    print('unable to show data')

myc.close()
conn.close()