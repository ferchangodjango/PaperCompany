from mysql.connector import Error
import mysql.connector
from randomData import Seller

try:
    conection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='papercompany'
    )
    cursor=conection.cursor()
    QUERY_SELLER=""" INSERT INTO sellers (NAME,LASTNAME,EMAILADRESS)
                    VALUES ( %s ,%s ,%s) """
    cursor.executemany(QUERY_SELLER,Seller)
    conection.commit()

except Exception as ex:
    raise Exception(ex)

finally:
    if conection.is_connected():
        conection.close()
        print("la conección ha sido cerrada")
    