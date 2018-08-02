import sqlite3 as sql
import vpizza
import nvpizza
#import pizzaClass
import Order
pizzas=[]
def displayChoice(name):
    print("1:VEG Pizza\n2:Non-Veg Pizza\n3:Order\n4:Logout ")
    pch=int(input("Enter your choice:"))

    if(pch==1):
        x=vpizza.selectPizza()
        print("\n")
        print(x.pname,x.total_price)
        pizzas.append(x)
        input()
        displayChoice(name)
    elif(pch==2):
        x=nvpizza.selectPizza()
        print("\n")
        print(x.pname,x.total_price)
        pizzas.append(x)
        input()
        displayChoice(name)
    elif(pch==3):
        #for y in pizzas:
            #print(y.pname,y.prize,y.quantity,y.total_price)
        Order.billgen(pizzas,name)
        print("\n\nThank you.....")
        print("\nSigning out....")
    elif(pch==4):
        print("\nSigning out....")
        exit()
    else:
        print("Enter valid Option...\n")
        input()
        displayChoice(name)

def loginUser():
    conn=sql.connect("pizza_db.db")
    cur=conn.cursor()
    name=None
    phone=input("Phone:")
    password=input("Password:")
    if (phone=="" and password==""):
        print("Please check username and password")
    else :
        query_1="select name,phone,password from customer"
        result=cur.execute(query_1)
        rows=cur.fetchall()
        #op in tuple
        for row in rows:
            if (row[1]==phone and  row[2]==password):
                flag=True
                name=row[0]
                #print("User valid")
                break
            else:
                flag=False

        if(flag==True):
            print("\n"*4)
            displayChoice(name)
        else:
            print("\nIncorrect Phone Number or password\nTry again....\n")
            loginUser()
#loginUser()
