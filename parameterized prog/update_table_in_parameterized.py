import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection....... successfully')
except:
    print('connection...... denied')

sql = 'update student SET stu_name=%s, stu_roll=%s, fees=%s where stu_id=%s'
myc = conn.cursor()
update_data = ('avesh', 122, 25500, 29)
myc.execute(sql, update_data)
try:
    conn.commit()
    print('save to data in databases')
    print(myc.rowcount, 'name is changed')

except:
    conn.rollback()                    # rollback tyare use thase jayare commit bai thay.
    print('unable to insert data')
myc.close()
conn.close()