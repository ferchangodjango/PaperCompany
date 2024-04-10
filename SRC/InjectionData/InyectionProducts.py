from mysql.connector import Error 
import mysql.connector
from randomData import ProductsPrice

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='papercompany')
    cursor=connection.cursor()
    QUERY_PRODUCTS="""INSERT INTO products (PRODUCTNAME,PRODUCTPRICE)
                    VALUES (%s, %s)"""
    cursor.executemany(QUERY_PRODUCTS,ProductsPrice)
    connection.commit()

except Exception as ex:
    raise Exception(ex)

finally:
    if connection.is_connected():       
        connection.close()
        print("La coneccion se cerro exitosamente.")