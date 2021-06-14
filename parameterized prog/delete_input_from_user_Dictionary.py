import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection....... successfully')
except:
    print('connection...... denied')

sql = 'delete from student where stu_id=%(id)s'
myc = conn.cursor()
n = int(input('Enter delete row stu_id :- '))
try:
    myc.execute(sql, {'id': n})
    conn.commit()
    print('save to data in databases')
    print('deleted Row count :', myc.rowcount)     # Rowcount print
except:
    conn.rollback()                    # rollback tyare use thase jayare commit bai thay.
    print('unable to delete data')
myc.close()
conn.close()
