import mysql.connector
import sys

class MainUpdate():
    def __init__(self):
        self.db_connect()

    def db_connect(self):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="4863km640per",
            database="work_with_me_5",
            charset='utf8',
        )
        global mycursor
        mycursor = mydb.cursor()

    def select_from_db(self):
        b = 0
        mycursor.execute("SELECT Code FROM ektos_cis_vendors WHERE Vendor = 'digi-key' OR Vendor = 'DigiKey'")
        for a in mycursor:
            print(a)
            b+=1
            print(b)


cis1 = MainUpdate()

print("TRALALA")








