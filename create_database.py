import mysql.connector
try:
    conn = mysql.connector.connect(user='root', password='Tejas@123',
                                   host='localhost', port=3306)
    if(conn.is_connected()):
        print("connction.... Sucessfully")

except:
    print("unable to connected")


myc = conn.cursor()
myc.execute('CREATE DATABASE employe')  # run nai thay becuse aa database me create kari nakhyo 6.

myc.close()
conn.close()