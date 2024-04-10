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
    QUERY_TABLE=""" CREATE TABLE sells (
                    IDSELLS INT NOT NULL AUTO_INCREMENT,
                    IDPRODUCTS INT,
                    IDSELLER INT,
                    QUANTITY INT,
                    PRIMARY KEY (IDSELLS))"""
    cursor=connection.cursor()
    cursor.execute(QUERY_TABLE)
    connection.commit()

except Exception as ex:
    raise Exception(ex)
finally:
    if connection.is_connected():
        connection.close()
        print('La coneccion se ha cerrado exitosamente')