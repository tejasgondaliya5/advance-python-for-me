import mysql.connector
try:
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', port=3306)
    print('connection.... Successfully')

except:
    print('Connection denied.')

myc = conn.cursor()
myc.execute('show databases')

for d in myc:
    print(d)

myc.close()
conn.close()