import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash

password1=generate_password_hash('perrosalchicha')
user='FERCHANGODJANGO'
data=[(user,password1)]

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='papercompany'
    )
    cursor=connection.cursor()
    QUERY_INYECTION="""INSERT INTO administrator (USERNAME,PASSWORD) 
                    VALUES (%s, %s)"""
    cursor.executemany(QUERY_INYECTION,data)
    connection.commit()


except Exception as ex:
    raise Exception(ex)
finally:
    if connection.is_connected():
        connection.close()
        print("La conección se ha cerrado exitosamente")