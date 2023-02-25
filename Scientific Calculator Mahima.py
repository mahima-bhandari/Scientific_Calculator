from tkinter import *
from math import sqrt
from math import e
from math import log

top=Tk()
top.title("Scientific Calculator")
top.geometry("500x500")
mytext=StringVar()
mytxt=StringVar()
mytxt1=IntVar()

La=Label(top,text="BINARY OPERATIONS",font=("bold",10),fg="red")
La.place(x=50,y=25)

l1=Label(top,text="Enter first number : ",fg="blue")
l1.place(x=50,y=50)
e1=Entry(top)
e1.place(x=175,y=50)

l2=Label(top,text="Enter second number : ",fg="green")
l2.place(x=50,y=80)
e2=Entry(top)
e2.place(x=175,y=80)

def fun():
    e3=int(e1.get())+int(e2.get())
    mytext.set("Addition : "+str(e3))

btn1=Button(top,text="+",width=4,bg="black",fg="white",activebackground="grey",command=fun)
btn1.place(x=50,y=130)

"""result=Label(top,textvariable=mytext)
result.place(x=100,y=300)"""

def fun1():
    e4=int(e1.get())-int(e2.get())
    mytext.set("Subtraction : "+str(e4))

btn2=Button(top,text="-",width=4,bg="white",fg="black",activebackground="grey",command=fun1)
btn2.place(x=100,y=130)

def fun2():
    e5=int(e1.get())*int(e2.get())
    mytext.set("Multiplication : "+str(e5))

btn3=Button(top,text="x",width=4,bg="black",fg="white",activebackground="grey",command=fun2)
btn3.place(x=150,y=130)

def fun3():
    e6=int(e1.get())/int(e2.get())
    mytext.set("Division : "+str(e6))

btn4=Button(top,text="/",width=4,bg="white",fg="black",activebackground="grey",command=fun3)
btn4.place(x=200,y=130)

def fun4():
    e7=int(e1.get())**int(e2.get())
    mytext.set("Power : "+str(e7))

btn5=Button(top,text="^",width=4,bg="white",fg="black",activebackground="grey",command=fun4)
btn5.place(x=50,y=175)

def fun5():
    e8=int(e1.get())//int(e2.get())
    mytext.set("Greatest Integer Function : "+str(e8))

btn1=Button(top,text="//",width=4,bg="black",fg="white",activebackground="grey",command=fun5)
btn1.place(x=100,y=175)
    
result=Label(top,textvariable=mytext,fg="green")
result.place(x=50,y=210)

Lb=Label(top,text="UNARY OPERATIONS",fg="red",font=("bold",10))
Lb.place(x=50,y=250)

lb1=Label(top,text="Enter a number : ",fg="blue")
lb1.place(x=50,y=280)
ety1=Entry(top)
ety1.place(x=150,y=280)

def fn():
    fact=1
    for i in range(int(ety1.get()),0,-1):
        fact=fact*i
    mytxt.set("Factorial : "+str(fact))

bt1=Button(top,text="!",width=4,fg="white",bg="black",activebackground="grey",command=fn)
bt1.place(x=50,y=330)

def fn1():
    s=sqrt(int(ety1.get()))
    mytxt.set("Square root : "+str(s))

bt2=Button(top,text="sqrt",width=4,fg="black",bg="white",activebackground="grey",command=fn1)
bt2.place(x=100,y=330)

def fn2():
    exp=e**(int(ety1.get()))
    mytxt.set("e^ : "+str(exp))

bt3=Button(top,text="e^",width=4,fg="white",bg="black",activebackground="grey",command=fn2)
bt3.place(x=150,y=330)

def fn3():
    x=int(ety1.get())
    lg=log(x)
    mytxt.set("ln value : "+str(lg))

bt4=Button(top,text="ln()",width=4,fg="black",bg="white",activebackground="grey",command=fn3)
bt4.place(x=200,y=330)

rslt=Label(top,textvariable=mytxt,fg="green")
rslt.place(x=50,y=380)

mahi=Label(top,text="MAHIMA BHANDARI'S",fg="purple",font=("bold",12))
mahi.place(x=50,y=420)

scicalc=Label(top,text="SCIENTIFIC CALCULATOR",fg="indigo",font=("bold",12))
scicalc.place(x=216,y=420)

top.mainloop()
