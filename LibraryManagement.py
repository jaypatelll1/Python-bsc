import mysql.connector
import sys

def CreatingDb():
    try:
        cur = con.cursor()
        cur.execute("create database workshop_demo")
        print("Database Created Successfully.....")
        cur.execute("show databases")
        dbs = cur.fetchall()
        for x in dbs:
            print(x)
    except:
        print("Connection error")

def InsertBook():
    try:
        con = mysql.connector.connect(host="localhost", user="root",password="", database="workshop_demo")
        print("Connection Successfully")
        cur = con.cursor()

        bookname= input("Enter the Book Name : ")
        author= input("Enter the Name of Author : ")

        sql = "insert into librarytable(bookname,author) values('{}','{}');".format(bookname,author)
        cur.execute(sql)
        print(cur.rowcount," Record inserted")
        con.commit()
    except:
        print("Error in Insert Book method")
    finally:
        if con:
            con.close()
            print("Resources released")

def CheckForBooks():
    try:
        con = mysql.connector.connect(host="localhost", user="root",password="", database="workshop_demo")
        print("Connection Successfully")
        cur = con.cursor()
        sql = "select * from librarytable"
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print("ID  : ",row[0],"\nBOOK NAME: ",row[1],"\nAUTHOR : ",row[2],"\n")
            print("---------------------------------------------------------------------------\n")
    except:
        print("Connection Error")
    finally:
        if con:
            con.close()
            print("Resources released")

def DeleteBooks():
    try:
        con = mysql.connector.connect(host="localhost", user="root",password="", database="workshop_demo")
        print("Connection Successfully")
        cur = con.cursor()
        bookname = input("Enter the Name of Book: ")
        author = input("Enter the Author Name: ")

        sql = "DELETE FROM librarytable WHERE bookname='{}' and author='{}'".format(bookname,author)
        cur.execute(sql)
        print(cur.rowcount," Record Deleted Successfully...")
        con.commit()
    except:
        print("Connection Error")
    finally:
        if con:
            con.close()
            print("Resources released")


def main():
    print("LIBRARY MANAGEMENT SYSTEM\n\n")
    print("Press 1 -> Create Database\nPress 2-> Insert Books\nPress 3-> See Available Books\nPress 4-> Delete Book\nPress 5-> Exit\n")
    print("======================================================================================\n")
    while True:
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            CreatingDb()
            print("======================================================================================\n")
        elif choice == 2:
            InsertBook()
            print("======================================================================================\n")
        elif choice == 3:
            CheckForBooks()
            print("======================================================================================\n")
        elif choice == 4:
            DeleteBooks()
            print("======================================================================================\n")
        elif choice == 5:
            print("Exting the Program...\n")
            print("======================================================================================\n")
            sys.exit(0)          
        else:
            print("Invalid Choice.\n")
            print("======================================================================================\n")

if __name__ =="__main__":
    main()
