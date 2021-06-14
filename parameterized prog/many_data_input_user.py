# take multiple input from user Tuple Format(%s, %s, %s)..........................

import mysql.connector


def student_data(name, roll, fees):
    try:
        conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', database='student',
                                        port=3306)
        print('connection ....... successfully')
    except:
        print('connection ........ denied')
    sql = 'insert into student(stu_name, stu_roll, fees) values(%s, %s, %s)'
    myc = conn.cursor()

    peram = (name, roll, fees)

    try:
        myc.execute(sql, peram)
        conn.commit()
    except:
        conn.rollback()
        print('insertion denied')

    myc.close()
    conn.close()


while True:
    name = input('Enter Student name :- ')
    roll = int(input('Enter you roll :- '))
    fees = float(input('Enter your Fees :- '))
    student_data(name, roll, fees)
    ans = input('Do you want to exit? (Y/N)')
    print()

    if(ans=='y'):
        break