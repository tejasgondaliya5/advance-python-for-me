# ama cursor ma buffered=True karvu pade naitar ERROR male.
# because myc.close() karyu pan ama haju thodik row baki hati fetch karva mate.
# tyare buffered cursor vaprava thi jetli row joti hoy te display thay ane baki ni behind the seen run thai jay.
# mate apn ne output ma row 3 print thase pan rowcount 5 thase.

import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection....... successfully')

except:
    print('connection.......... filed')

myc = conn.cursor(buffered=True)

try:
    myc.execute('select * from student')
    rows = myc.fetchmany(size=3)
    for i in rows:
        stu_id = i[0]
        stu_name = i[1]
        stu_roll = i[2]
        fess = i[3]
        print(f'student ID = {stu_id} : student NAME = {stu_name} : student rollno. = {stu_roll} : fess = {fess}')
    print('total rows :', myc.rowcount)


except:
    conn.rollback()
    print('unable to show data')

myc.close()
conn.close()