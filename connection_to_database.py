import mysql.connector
try:
    conn = mysql.connector.connect(user='root', password='Tejas@123',
                                   host='localhost', database='student',
                                   port=3306)
    if (conn.is_connected()):
        print('connection..... Successfully with database')

except:
    print('connection denied')

conn.close()