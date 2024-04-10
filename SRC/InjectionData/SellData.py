from mysql.connector import Error
import mysql.connector
import pandas as pd
import numpy as np

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='papercompany'
    )
    QUERY="""SELECT IDSELLER
            FROM sellers"""
    DataSellers=pd.read_sql_query(QUERY,connection)
    

except Exception as ex:
    raise Exception(ex)

finally:
    if connection.is_connected():
        connection.close()
        #print("La conección fue cerrada exitosamente")

#print(DataSellers)
