import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", user="root",password="", database="workshop_demo")
    print("Connection successfully")
    cur = con.cursor()
    print(cur)
    sql = "DELETE FROM tpolybse WHERE name='Jignesh'"
    cur.execute(sql)
    print(cur.rowcount," Record Deleted Successfully...")
    con.commit()
except:
    print("Connection Error")
    con.rollback()
finally:
    if con:
        con.close()
        print("Resources released")