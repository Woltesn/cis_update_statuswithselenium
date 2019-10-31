import mysql.connector
import sys
import time
import  os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

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
        self.select_from_db()

    def select_from_db(self):
        driver = WebDriver(executable_path='C:\dpe\Chromdriver\chromedriver.exe')
        mycursor.execute("SELECT Code FROM ektos_cis_vendors WHERE Vendor = 'digi-key' OR Vendor = 'DigiKey'")
        masiv = []
        for vendor_code in mycursor:
            b = str(vendor_code)
            fixed1 = ''.join(b.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed4 = ''.join(fixed3.split(","))
            masiv.append(fixed4)
        print(masiv)
        for a in masiv:
            print(a)
            time.sleep(0.2)
            driver.get('https://www.digikey.com/')  # Open Google.com in Google Chrome browser
            find_serch = driver.find_element_by_xpath(
                '//*[@id="main-layout-content"]/div[1]/div/div[2]/div[2]/div[2]/input')  # Search for input on a web page
            find_serch.send_keys(a)
            find_serch.send_keys(Keys.ENTER)
            time.sleep(0.2)
            try:
                find_part_status = driver.find_element_by_xpath("//*[contains(.,'Part Status')]")
                try:
                    find_actie_status  = driver.find_element_by_xpath("//*[contains(.,'Active')]")
                    mycursor.execute(
                        mycursor.execute("UPDATE ektos_cis SET Status = '' WHERE Part_Number = (SELECT Part_Number FROM ektos_cis_vendors WHERE Code = '{}')".format(a)))

                except Exception:
                    mycursor.execute("UPDATE ektos_cis SET Status = 'OBSOLETE' WHERE Part_Number = (SELECT Part_Number FROM ektos_cis_vendors WHERE Code = '{}')".format(a))


            except Exception:
                print("The text is not found on the page!")
                handle = open("should_be_check.txt", "a")
                handle.write(a+'\n')
                handle.close()
            print("___________________________________")

cis1 = MainUpdate()










