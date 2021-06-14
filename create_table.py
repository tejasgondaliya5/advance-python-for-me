# output ma ERROR avse because ek var table create thai gayu 6.
import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123',
                                    host='localhost', database='student',
                                   port=3306)
    if (conn.is_connected()):
        print('connection...... successfully.')
except:
    print('connection.... denied')

sql = 'CREATE TABLE student1(stu_id INT AUTO_INCREMENT PRIMARY KEY, stu_name VARCHAR(20), stu_roll INT, fees FLOAT)'

myc = conn.cursor()
myc.execute(sql)


myc.close()
conn.close()