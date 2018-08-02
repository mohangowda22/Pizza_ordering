
def billgen(pizzas,name):
 import time

 from reportlab.lib.pagesizes import letter
 from reportlab.pdfgen import canvas
 g_total=0
 for pizza in pizzas:
     g_total=g_total+pizza.total_price
 cname="Customer Name:"+name.upper()
 billname="Generated_Bills/bill_"+name+".pdf"
 canvas=canvas.Canvas(billname,pagesize=letter)
 canvas.setFont('Helvetica', 15)
 canvas.line(20,700,580,700)
 canvas.drawString(270,670,'XYZ Pizzas')
 canvas.drawString(250,650,'Rajajinagar Phase3')
 localtime = time.asctime( time.localtime(time.time()) )
 canvas.drawString(20,610,str(localtime))
 canvas.drawString(350,610,cname)
 canvas.line(20,590,580,590)
 canvas.line(20,565,580,565)
 canvas.drawString(20,570,'Name of pizza')
 canvas.drawString(210,570,'Price')
 canvas.drawString(340,570,'Qty')
 canvas.drawString(500,570,'Total')
 i=550
 for pizza in pizzas:
     canvas.drawString(20,i,pizza.pname)
     canvas.drawString(210,i,str(pizza.prize))
     canvas.drawString(340,i,str(pizza.quantity))
     canvas.drawString(500,i,str(pizza.total_price))
     i=i-20
     j=i-20
 canvas.line(20,j,580,j)
 i-=20
 canvas.drawString(400,i-20,"Grand Total:"+str(g_total))
 canvas.save()
