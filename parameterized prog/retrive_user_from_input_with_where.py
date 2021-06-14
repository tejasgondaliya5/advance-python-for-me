import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123',host='localhost', database='student', port=3306)
    print('connection....... successfully')

except:
    print('connection.......... filed')
sql = 'select * from student where stu_id=%s'
myc = conn.cursor()
n = int(input('Enter student id to display :- '))
disp_value = (n,)
try:
    myc.execute(sql, disp_value)
    row = myc.fetchone()
    while row is not None:
        stu_id = row[0]
        stu_name = row[1]
        stu_roll = row[2]
        fees = row[3]
        print(f'student_id = {stu_id} : stu_name = {stu_name} : stu_rollno = {stu_roll} : fess = {fees}')
        row = myc.fetchone()
except:
    conn.rollback()
    print('unable to show data')

myc.close()
conn.close()