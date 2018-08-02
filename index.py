import sqlite3 as sql
import login
import signup


def createDatabase():
    conn=sql.connect("pizza_db.db")
    sqlQuery="create table if not exists customer(name char(100),phone char(12),password char(20),address char(1000),primary key(phone))"
    conn.execute(sqlQuery)
    conn.commit()
    conn.close()
def mainProgram():
    print("***Welcome***\n")
    createDatabase()
    ch=int(input("\n1:Login\n2:Signup\n3:Exit\n\nEnter your choice:"))
    if(ch==1):
         login.loginUser()
         input()
         mainProgram()
    elif(ch==2):
        signup.signupUser()
        input()
        mainProgram()
    elif(ch==3):
        exit()
    else:
        print("\nPlease select a valid option....")
mainProgram()
