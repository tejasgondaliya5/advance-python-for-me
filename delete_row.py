'''
this program change DELETE sql qurrey.
'''
import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection....... successfully')
except:
    print('connection...... denied')

sql = 'delete from student where stu_id=8'    # 8 no. ni id ma ravi hato te delete thai gayo.
myc = conn.cursor()
myc.execute(sql)
try:
    conn.commit()
    print('save to data in databases')
    print('deleted Row count :', myc.rowcount)     # Rowcount print
except:
    conn.rollback()                    # rollback tyare use thase jayare commit bai thay.
    print('unable to delete data')
myc.close()
conn.close()
