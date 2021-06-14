
import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection....... successfully')
except:
    print('connection...... denied')

sql = 'insert into student(stu_name, stu_roll, fees) VALUES("Harsh", 104, 10000.52)'
myc = conn.cursor()
myc.execute(sql)
try:
    conn.commit()
    print('save to data in databases')
    print('last Row_id :', myc.lastrowid)     # show last primary key id
except:
    conn.rollback()                    # rollback tyare use thase jayare commit bai thay.
    print('unable to insert data')
myc.close()
conn.close()