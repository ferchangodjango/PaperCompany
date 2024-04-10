import mysql.connector 
from mysql.connector import Error

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='papercompany'
    )
    cursor=connection.cursor()
    QUERY_ADMINISTRATOR="""CREATE TABLE administrator (
                            IDADMIN INT NOT NULL AUTO_INCREMENT,
                            USERNAME VARCHAR(45),
                            PASSWORD CHAR(200),
                            PRIMARY KEY(IDADMIN))"""
    cursor.execute(QUERY_ADMINISTRATOR)
    connection.commit()
except Exception as ex:
    raise Exception(ex)

finally:
    if connection.is_connected():
        connection.close()
        print("La conección se ha cerrado exitosamente")