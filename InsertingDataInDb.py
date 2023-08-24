import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", user="root",password="", database="workshop_demo")
    print("Connection successfully")
    cur = con.cursor()
    print(cur)

    name= input("Enter the name: ")
    sem= int(input("Enter the sem: "))
    city= input("Enter the city:" )

    sql = "insert into tpolybse(name,sem,city) values('{}',{},'{}');".format(name,sem,city)
    cur.execute(sql)
    print(cur.rowcount," Record inserted")
    con.commit()
except:
    print("Connection Error")
    con.rollback()
finally:
    if con:
        con.close()
        print("Resources released")