import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123',host='localhost', database='student', port=3306)
    print('connection....... successfully')

except:
    print('connection.......... filed')

myc = conn.cursor()

try:
    myc.execute( 'select * from student' )
    rows = myc.fetchall()
    print(rows)

    # ......................................
    for i in rows:           # badha data ek sathe fetch thai row ma avi jay jyare fetchone ma only on line no data fetch thai ne ave.
        stu_id = i[0]
        stu_name = i[1]
        stu_roll = i[2]
        fess = i[3]
        print(f'student ID = {stu_id} : student NAME = {stu_name} : student rollno. = {stu_roll} : fess = {fess}')

    print('total rows:', myc.rowcount)

except:
    conn.rollback()
    print('unable to show data')

myc.close()
conn.close()