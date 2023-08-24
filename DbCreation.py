import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", user="root",password="")
    print("Connection successfully")
    cur = con.cursor()
    cur.execute("create database workshop_demo")
    print("1")
    cur.execute("show databases")
    dbs = cur.fetchall()
    for x in dbs:
        print(x)
except:
    print("Connection Error")