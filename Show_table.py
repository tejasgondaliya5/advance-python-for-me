import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123',
                                    host='localhost', database='student',
                                   port=3306)
    if (conn.is_connected()):
        print('connection...... successfully.')
except:
    print('connection.... denied')

sql1 = 'SHOW TABLES'
myc1 = conn.cursor()

myc1.execute(sql1)

for i in myc1:
    print(i)
myc1.close()
conn.close()