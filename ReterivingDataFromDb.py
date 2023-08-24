import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", user="root",password="", database="workshop_demo")
    print("Connection successfully")
    cur = con.cursor()
    print(cur)
    sql = "select * from tpolybse"
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        print("ID  : ",row[0],"\nNAME: ",row[1],"\nSEM : ",row[2],"\nCITY: ",row[3],"\n")
        print("---------------------------------------------------------------------------\n")
        #print("%d     %s     %s     %s"%(row[0],row[1],row[2],row[3]))
except:
    print("Connection Error")
finally:
    if con:
        con.close()
        print("Resources released")