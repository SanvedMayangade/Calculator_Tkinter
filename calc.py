from tkinter import * 

root = Tk()
root.title('Calculator')
root.geometry('400x600+300+300')

display=StringVar()
globalVar=""

def add_value_fun(value):

    global globalVar
    globalVar +=str(value)

    display.set(globalVar)

def Clear():
    global globalVar
    globalVar=""

    display.set(globalVar)

def get_answer_fun():
    global globalVar
    result=str(eval(globalVar))

    display.set(result)
    globalVar=result



displaylabel=Label(root,textvariable=display,font=("roboto",20,"bold"),bg="#cfe2f3",padx=20,pady=10,borderwidth=10,relief="sunken")
displaylabel.pack(fill=X)

btn_ac=Button(root,text="ac",font=("roboto",22,"bold"),bg="#cfe2f3",padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:Clear())
btn_ac.pack(fill=X)

btn1=Button(root,text='1',font=('sarifsans',22,'bold'),bg='pink',padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun(1))
btn1.place(x=20,y=160)

btn2=Button(root,text='2',font=('sarifsans',22,'bold'),bg='pink',padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun(2))
btn2.place(x=110,y=160)

btn3=Button(root,text='3',font=('sarifsans',22,'bold'),bg='pink',padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun(3))
btn3.place(x=200,y=160)

btn_add=Button(root,text="+",font=("roboto",22,"bold"),bg="pink",padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun("+"))
btn_add.place(x=290,y=160)

btn4=Button(root,text='4',font=('sarifsans',22,'bold'),bg='pink',padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun(4))
btn4.place(x=20,y=260)

btn5=Button(root,text='5',font=('sarifsans',22,'bold'),bg='pink',padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun(5))
btn5.place(x=110,y=260)

btn6=Button(root,text='6',font=('sarifsans',22,'bold'),bg='pink',padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun(6))
btn6.place(x=200,y=260)

btn_sub=Button(root,text="-",font=("roboto",22,"bold"),bg="pink",padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun("-"))
btn_sub.place(x=290,y=260)

btn7=Button(root,text='7',font=('sarifsans',22,'bold'),bg='pink',padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun(7))
btn7.place(x=20,y=360)

btn8=Button(root,text='8',font=('sarifsans',22,'bold'),bg='pink',padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun(8))
btn8.place(x=110,y=360)

btn9=Button(root,text='9',font=('sarifsans',22,'bold'),bg='pink',padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun(9))
btn9.place(x=200,y=360)

btn_mul=Button(root,text="*",font=("roboto",22,"bold"),bg="pink",padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun("*"))
btn_mul.place(x=290,y=360)

btn0=Button(root,text=0,font=("roboto",22,"bold"),bg="pink",padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun(0))
btn0.place(x=20,y=460)

btn_div=Button(root,text="/",font=("roboto",22,"bold"),bg="pink",padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:add_value_fun("/"))
btn_div.place(x=110,y=460)

btn_back=Button(root,text="c",font=("roboto",22,"bold"),bg="pink",padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:Clear("c"))
btn_back.place(x=200,y=460)

btn_equal=Button(root,text="=",font=("roboto",22,"bold"),bg="blue",padx=8,pady=8,borderwidth=6,relief="raised",command=lambda:get_answer_fun())
btn_equal.place(x=290,y=460)
# btn_equal.pack(fill=Y)



root.mainloop()