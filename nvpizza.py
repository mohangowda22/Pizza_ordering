import sqlite3 as sql
import pizzaClasss

def selectPizza():
    sqlQuery_1="select * from nvegpizza"
    conn=sql.connect("pizza_db.db")
    cur=conn.cursor()
    cur.execute(sqlQuery_1)
    data=cur.fetchall()

    print("Select Pizza From Below")
    c=1
    print("\nSl.no\t\tName\t\tPrice\n")
    for d in data:
        print(c,"\t",d[0],"\t",d[1])
        c+=1
    c=c-1;
    #print(c)
    s_pizza=int(input("\nEnter the pizza no.:"))
    quantity_pizza=int(input("\nEnter the quantity:"))
    x=1
    #print(data)
    g=None
    for d in data:
        #print(d)
        if(x==s_pizza):
            obj_p=pizzaClasss.Pizza()
            obj_p.pname=d[0]
            obj_p.prize=d[1]
            obj_p.quantity=quantity_pizza
            obj_p.total_price=quantity_pizza*int(d[1])
            return obj_p
            #g=obj_p
        x+=1
    #print(g.pname,g.prize,g.total_price)
#selectPizza()
