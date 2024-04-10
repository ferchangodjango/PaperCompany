import mysql.connector 
from mysql.connector import Error
from UnionSells import TOTAL_SELLER

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='papercompany'
    )
    QUERY_INJECTION=""" INSERT INTO sells (IDPRODUCTS,IDSELLER,QUANTITY)
                        VALUES (%s, %s, %s)"""
    cursor=connection.cursor()
    cursor.executemany(QUERY_INJECTION,TOTAL_SELLER)
    connection.commit()

except Exception as ex:
    raise Exception(ex)

finally:
    if connection.is_connected():
        connection.close()
        print('la conección se ha cerrado exitosamente')