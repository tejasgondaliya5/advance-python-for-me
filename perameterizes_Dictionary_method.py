'''
what is difference between tuple or dictionary :-
          - tuple argument is mention order.
          -but Dictionary is free for change argument order. EX:- first enter roll, second name , third fees so it can
           work.
'''
import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student', port=3306)
    print('connection ....... successfully')
except:
    print('connection ........ denied')
sql = 'insert into student(stu_name, stu_roll, fees) values(%(n)s, %(r)s, %(f)s)'

myc = conn.cursor()

peram = {'n': 'janvi', 'r': 114, 'f': 15500}
try:
    myc.execute(sql, peram)
    conn.commit()
except:
    conn.rollback()
    print('insertion denied')

myc.close()
conn.close()