import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd
import openpyxl
from sqlalchemy import create_engine
import csv
from pymongo import MongoClient
import logging
import log.log
def data_frame_read():
    try:
        logging.info("Read dataset as a dataframe....")
        db = mysql.connect(host = "Localhost", user = "root", passwd = "Hannah_0027", use_pure = True)
        query1 = pd.read_sql('select * from textile.attribute_dataset', db)
        query2 = pd.read_sql('select * from textile.dress_sales', db)
        attribute_dataset = pd.DataFrame(query1, columns = ['Dress_ID', 'Style', 'Price','Rating','Size','Season','NeckLine',
                                        'SleeveLength','waiseline','Material','FabricType','Decoration',
                                        'Pattern_Type','Recommendation'])
        dress_sales = pd.DataFrame(query2, columns = ['Dress_ID','29-8-2013','31-8-2013','9-2-2013','9-4-2013','9-6-2013','9-8-2013','9-10-2013','9-12-2013','14-9-2013','16-9-2013','18-9-2013','20-9-2013','22-9-2013','24-9-2013','26-9-2013','28-9-2013','30-9-2013','10-2-2013','10-4-2013','10-6-2013','10-8-2010','10-10-2013','10-12-2013'])
        print(attribute_dataset)
        #print(dress_sales)
    except Error as e:
        logging.info("Error while reading the dataset as a dataframe....", e)
        print("Error while reading the dataset as a dataframe....", e)

def convert_into_json():
    try:
        logging.info("Convert to json file")
        df = pd.read_excel(r'C:\Users\ASUS\Desktop\code\data science\data fsds\Attribute DataSet.xlsx')
        df = df.astype(object).where(pd.notnull(df), None)
        df.to_json('F:\Attribute_DataSet.json')
        logging.info("A json file created in the F drive with the file name is Attribute_DataSet.json")
        df1 = pd.read_json(r'F:/Attribute_DataSet.json')
        logging.info(f"JSON file...{df1}")
    except Error as e:
        logging.info("Error while converting to json file : ", e)
        print("Error while converting to json file : ", e)

def insert_into_mongodb():
    try:
        logging.info("File inserted into MongoDB Tables.....")
        df = pd.read_excel(r'C:\Users\ASUS\Desktop\code\data science\data fsds\Attribute DataSet.xlsx')
        # df.to_csv("F:\Attribute DataSet.csv" )
        df1 = pd.DataFrame(pd.read_csv("F:\Attribute DataSet.csv", index_col=0))
        logging.info(f"Data frame for Attribute_DataSet....{df1}")
        logging.info(f"You're connecting to mongoDB....")
        client = MongoClient(
            "mongodb+srv://GIRIJAOK:Hannah_0027@cluster0.ptn1r.mongodb.net/?retryWrites=true&w=majority")
        db = client.Task
        logging.info(f"A table created into mongoDB....")
        header = df1.head()
        table = open('F:\Attribute DataSet.csv', 'r')
        reader = csv.DictReader(table)
        db.segment.drop()
        for each in reader:
            row = {}
            for field in header:
                row[field] = each[field]
            db.Attribute_DataSet.insert_one(row)
            # logging.info(f"Values inserted into mongoDB....{row}")
            print(row)
    except Error as e:
        logging.info("Error while inserting data into mongodb....", e)
        print("Error while inserting data into mongodb....", e)

def left_join():
    try:
        logging.info("Performing left join operation with Attribute dataset and dress dataset on column Dress_ID....")
        conn = mysql.connect(host='localhost', database='textile', user='root', password='Hannah_0027')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            logging.info(f"You're connected to database:  {record}")
            cursor.execute("select * from attribute_dataset left join dress_sales on attribute_dataset.Dress_ID = dress_sales.Dress_ID order by  attribute_dataset.Dress_ID;")
            result = cursor.fetchall()
            for x in result:
                  print(" Result of Left Join...", x)
    except Error as e:
        logging.info("Sql query error for left join operation ....", e)
        print("Sql query error for left join operation ....", e)
def unique_dress():
    try:
        logging.info(f"finding how many unique dress that we have based on Dress_ID....")
        conn = mysql.connect(host='localhost', database='textile', user='root', password='Hannah_0027')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(" select count(distinct(dress_id)) from attribute_dataset;")
            result1 = cursor.fetchall()
            for i in result1:
                  print(" Result of distinct Dress Id: ", i)
    except Error as e:
        logging.info("Sql query error for distinct operation ....", e)
        print("Sql query error for distinct operation....", e)
def recommendation_dress():
    try:
        logging.info("Finding how many dress is having recommendation as 0....")
        conn = mysql.connect(host='localhost', database='textile', user='root', password='Hannah_0027')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select count(*) from attribute_dataset where Recommendation=0;")
            result2 = cursor.fetchall()
            for i in result2:
                print(" Result of dress is having recommendation as 0 : ", i)
    except Error as e:
        logging.info("Sql query error for count operation ....", e)
        print("Sql query error for count operation....", e)

def  total_sales_dress_id():
    try:
        logging.info(" finding  total dress sales for each and every Dress_ID and third highest most selling Dress_ID....")
        conn1 = create_engine('mysql+pymysql://root:Hannah_0027@localhost/textile')

        df1 = pd.read_sql('select * from textile.dress_sales', conn1)
        # df1= df1.astype(object).where(pd.notnull(df1), None)
        df = pd.DataFrame(df1,
                          columns=['Dress_ID', '29-8-2013', '31-8-2013', '9-2-2013', '9-4-2013', '9-6-2013', '9-8-2013',
                                   '9-10-2013', '9-12-2013', '14-9-2013', '16-9-2013', '18-9-2013', '20-9-2013',
                                   '22-9-2013', '24-9-2013', '26-9-2013', '28-9-2013', '30-9-2013', '10-2-2013',
                                   '10-4-2013', '10-6-2013', '10-8-2010', '10-10-2013', '10-12-2013'])
        #print(df)
        col_list = list(df)
        df['Sum'] = df[col_list].sum(axis=1)
        print(df)
        logging.info(f"Table with total sales for individual dress id....{df}")
        a = df['Sum'].nlargest(3)
        print(" First three largest sales id's : ", a)
        logging.info(f"First three highest sales id's with total : {a}")
        s = a.idxmin()
        print("The third largest sales id is : ", s)
        logging.info(f"Third highest dress sale total is : {s}")
        b = sorted(df['Sum'])[-3]
        print("3rd largest Sales id: ", b)
        logging.info(f"Third highest dress sale dress id is : {b}")

    except Error as e:
        logging.info("Error while finding total and 3rd highest id.....",e)
        print("Error while finding total and 3rd highest id....", e)
data_frame_read()
convert_into_json()
insert_into_mongodb()
left_join()
unique_dress()
recommendation_dress()
total_sales_dress_id()