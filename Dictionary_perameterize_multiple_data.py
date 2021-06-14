import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection ....... successfully')
except:
    print('connection ........ denied')
sql = 'insert into student(stu_name, stu_roll, fees) values(%(n)s, %(r)s, %(f)s)'

myc = conn.cursor()

peram = [{'n': 'janvi', 'r': 114, 'f': 15500},
         {'n': 'uravi', 'r': 115, 'f': 15500},
         {'n': 'dhruvita', 'r': 115, 'f': 15500}]                # list of dictionary
try:
    myc.executemany(sql, peram)         # executemany() method use
    conn.commit()
except:
    conn.rollback()
    print('insertion denied')

myc.close()
conn.close()