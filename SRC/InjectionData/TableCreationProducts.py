from mysql.connector import Error
import mysql.connector

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='papercompany')
    QUERY_TABLE_PRODUCTS=""" CREATE TABLE products (
                            IDPRODUCTS INT NOT NULL AUTO_INCREMENT,
                            PRODUCTNAME VARCHAR(45),
                            PRODUCTPRICE REAL,
                            PRIMARY KEY(IDPRODUCTS))"""
    cursor=connection.cursor()
    cursor.execute(QUERY_TABLE_PRODUCTS)
    connection.commit()
    

except Exception as ex:
    raise Exception(ex)

finally:
    if connection.is_connected():
        connection.close()
        print('Conección cerrada exitosamente')
