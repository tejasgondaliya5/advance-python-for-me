import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection ....... successfully')
except:
    print('connection ........ denied')
sql = 'insert into student(stu_name, stu_roll, fees) values(%s, %s, %s)'
myc = conn.cursor()
peram = [("mihir", 107, 20500),("kuldip", 108, 25500),("Rahul", 109, 30500)]      # data is list of tuple format
try:
    myc.executemany(sql, peram)             # change executemany()
    conn.commit()
except:
    conn.rollback()
    print('insertion denied')

myc.close()
conn.close()