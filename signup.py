import sqlite3 as sql


def signupUser():
    conn=sql.connect("pizza_db.db")
    name=input("Enter your name:")
    phone=input("Enter your phone number:")
    address=input("Enter your address:")
    password=Checkpassword()

    sqlQuery_1="insert into customer values(?,?,?,?)"
    values=(name,phone,password,address)
    try:
        conn.execute(sqlQuery_1,values)
        conn.commit()
    except:
        print("\nSomething went worng.....\nTry again...")

def Checkpassword():
    password=input("Enter your password:")
    rpassword=input("Repeat your password:")
    if(password==rpassword):
        return password
    else:
        print("\nBoth Password did not match\nTry again\n")
        Checkpassword()
