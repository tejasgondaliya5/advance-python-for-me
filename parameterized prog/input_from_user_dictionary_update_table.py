import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection....... successfully')
except:
    print('connection...... denied')

sql = 'update student SET stu_name=%(name)s, stu_roll=%(roll)s, fees=%(fees)s where stu_id=%(id)s'
myc = conn.cursor()
id = int(input('Enter student ID to update :- '))
name = input('Enter Student Name :- ')
roll = input('Enter student Roll no:- ')
fees = input('Enter student Fees:- ')
update_data = {'name': name, 'roll': roll, 'fees': fees, 'id': id}
myc.execute(sql, update_data)
try:
    conn.commit()
    print('save to data in databases')
    print(myc.rowcount, 'row is changed')

except:
    conn.rollback()                    # rollback tyare use thase jayare commit bai thay.
    print('unable to insert data')
myc.close()
conn.close()