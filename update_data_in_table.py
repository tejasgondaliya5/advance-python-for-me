import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection....... successfully')
except:
    print('connection...... denied')

sql = 'update student SET stu_name="rajavi" where stu_id=7'
myc = conn.cursor()
myc.execute(sql)
try:
    conn.commit()
    print('save to data in databases')
    print(myc.rowcount, 'name is changed')

except:
    conn.rollback()                    # rollback tyare use thase jayare commit bai thay.
    print('unable to insert data')
myc.close()
conn.close()