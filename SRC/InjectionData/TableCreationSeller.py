from mysql.connector import Error
import mysql.connector 

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='papercompany')
    QUERY_CREATION=""" CREATE TABLE  SELLERS(
                    IDSELLER INT NOT NULL AUTO_INCREMENT,
                    NAME VARCHAR(45),
                    LASTNAME VARCHAR (45),
                    EMAILADRESS VARCHAR(45),
                    PRIMARY KEY(IDSELLER))"""
    cursor=connection.cursor()
    cursor.execute(QUERY_CREATION)
    
except Exception as ex:
    raise Exception(ex)

finally:
    if connection.is_connected():
        connection.close()
        print('La conección a sido cerrada')