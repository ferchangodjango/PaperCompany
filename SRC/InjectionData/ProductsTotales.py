from mysql.connector import Error
import mysql.connector
import pandas as pd

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='papercompany'
    )
    QUERY_PRODUCTS=""" SELECT *
                FROM products"""
    DataProducts=pd.read_sql_query(QUERY_PRODUCTS,connection)



except Exception as ex:
    raise Exception(ex)

finally:
    if connection.is_connected():
        connection.close()
        #print("Las coneccion se ha cerrado exitosamente")
