import mysql.connector

try:

    # create a connection to database
    conn = mysql.connector.connect(user='root', password='Tejas@123', host='localhost', port=3306)

    # show your connection is Establish or not.
    if (conn.is_connected()):
        print("connected successfully with MySQL")

    else:
        print("your device is not connected")
except:
    print("unable to connect")

conn.close()  # close connection
print(conn.is_connected())   # this function know about our connection connected or not




# config = {'user': 'root', 'password': 'Tejas@123', 'host': 'localhost', 'port': '3306'}
# try:
#     conn = mysql.connector.connect(**config)
#     if (conn.is_connected()):
#         print("connected succesfully")
#
#     else:
#         print("your device is not connected")
#
# except:
#     print( "unable to connect" )
