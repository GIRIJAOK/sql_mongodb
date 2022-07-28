import pandas as pd
import mysql.connector as mysql
import logging
from mysql.connector import Error
import log.log
def database_creation():
    try:
        logging.info(f"DATABASE CREATION....")
        mydb = mysql.connect(host = "localhost" , user ="root" , passwd = "Hannah_0027" )
        if mydb.is_connected():
            cursor = mydb.cursor()
            cursor.execute("CREATE DATABASE if not exists textile")
            logging.info(f"DATABASE IS CREATED WITH NAME textile....")
            print("Database is created")
    except Exception as e:
        logging.info("Error while connecting to MySQL... ",e)
        print("Error while connecting to MySQL...", e)

def attribute_table():
    try:
        logging.info(f"Creation of table Attribute DataSet....")
        conn = mysql.connect(host='localhost', database='textile', user='root', password='Hannah_0027')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            logging.info(f"You're connected to database:  {record}")
            print('Creating table with name attribute_dataset....')
            logging.info("Creating table with name attribute_dataset....")
            s = "create table if not exists textile.attribute_dataset( Dress_ID int(10) , Style varchar(30) , Price varchar(30) , Rating varchar(30), Size varchar(30) , Season varchar(30) , NeckLine varchar(80) , SleeveLength varchar(30) , waiseline varchar(30) , Material varchar(80) , FabricType varchar(30) , Decoration varchar(30),Pattern_Type varchar(30),Recommendation int(10))"
            cursor.execute(s)
            logging.info(f"Table is created with table name attribute_dataset....")
            print("Table is created....")
            df = pd.read_excel(r'C:\Users\ASUS\Desktop\code\data science\data fsds\Attribute DataSet.xlsx')
            df = df.astype(object).where(pd.notnull(df), None)
            for i, row in df.iterrows():
                sql = "INSERT INTO textile.attribute_dataset(Dress_ID ,Style,Price , Rating ,Size ,Season ,NeckLine ,SleeveLength, waiseline , Material , FabricType , Decoration , Pattern_Type ,Recommendation ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, tuple(row))
            conn.commit()
            df1 = pd.read_sql("select * from attribute_dataset",conn)
            logging.info(f"Attribute DataSet:{df1} ")
            print("Records inserted",df1)

    except Error as e:
        logging.info("Error while Creating the table Attribute DataSet....", e)
        print("Error while Creating the table Attribute DataSet....", e)

def dress_sales_table():
    try:
        logging.info(f"Creation of table Dress_Sales....")
        conn = mysql.connect(host='localhost', database='textile', user='root', password='Hannah_0027')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            logging.info(f"You're connected to database:  {record}")
            logging.info("Creating table with name dress_sales....")
            s = "create table if not exists textile.dress_sales( Dress_ID int , `29-8-2013` varchar(80) , `31-8-2013` varchar(80), `9-2-2013` varchar(80) , `9-4-2013` varchar(80) , `9-6-2013` varchar(80) , `9-8-2013` varchar(80) , `9-10-2013` varchar(80) , `9-12-2013` varchar(80) , `14-9-2013` varchar(80), `16-9-2013` varchar(80) , `18-9-2013` varchar(80) , `20-9-2013` varchar(80) , `22-9-2013` varchar(80) , `24-9-2013` varchar(80) , `26-9-2013` varchar(80) , `28-9-2013` varchar(80) , `30-9-2013` varchar(80) , `10-2-2013` varchar(80) , `10-4-2013` varchar(80) , `10-6-2013` varchar(80) , `10-8-2010` varchar(80), `10-10-2013` varchar(80) , `10-12-2013` varchar(80) )"
            cursor.execute(s)
            logging.info(f"Table is created with table name dress_sales....")
            print("Table is created....")
            df = pd.read_excel(r"C:\Users\ASUS\Desktop\code\data science\data fsds\Dress Sales.xlsx")
            df = df.astype(object).where(pd.notnull(df), None)
            for i, row in df.iterrows():
                sql = "INSERT INTO textile.dress_sales(Dress_ID ,`29-8-2013` , `31-8-2013` ,`9-2-2013` ,`9-4-2013` ,`9-6-2013` ,`9-8-2013`, `9-10-2013` , `9-12-2013` , `14-9-2013`, `16-9-2013` ,`18-9-2013` ,`20-9-2013`,`22-9-2013` ,`24-9-2013`,`26-9-2013` ,`28-9-2013`, `30-9-2013`,`10-2-2013`,`10-4-2013`,`10-6-2013`,`10-8-2010`,`10-10-2013`,`10-12-2013`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, tuple(row))
            conn.commit()
            df2 = pd.read_sql("select * from dress_sales", conn)
            logging.info(f"Dress Sales Dataset:{df2} ")
            print("Records inserted",df2)
    except Error as e:
        logging.info("Error while Creating the table Dress_Sales....", e)
        print("Error while Creating the table Dress_Sales....", e)

database_creation()
attribute_table()
dress_sales_table()

