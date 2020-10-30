from tkinter import *
root = Tk()

root.title("My Calculator")
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=30,pady=10)
#e.insert(0,"Enter the amount")

#Functions to perform operations

def Button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_Clear():
    e.delete(0,END)

def button_Add():
    first_number = e.get()
    global f_num
    global  math
    math = "Addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_Equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "Addition":
        e.insert(0,f_num + int(second_number))
    if math == "Substraction":
        e.insert(0,f_num - int(second_number))
    if math == "Multiplication":
        e.insert(0,f_num * int(second_number))
    if math == "Division":
        e.insert(0,f_num / int(second_number))

def button_Sub():
    first_number = e.get()
    global f_num
    global math
    math = "Substraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_Mul():
    first_number = e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_Div():
    first_number = e.get()
    global f_num
    global math
    math = "Division"
    f_num = int(first_number)
    e.delete(0, END)


#Define Buttons

button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: Button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: Button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: Button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: Button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: Button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: Button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: Button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: Button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: Button_click(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: Button_click(0))

button_clear = Button(root,text="CLEAR",padx=26,pady=20,command=button_Clear)
button_equal = Button(root,text="=",padx=40,pady=20,command=button_Equal)

button_add = Button(root,text="+",padx=40,pady=20,command=button_Add)
button_sub = Button(root,text="-",padx=40,pady=20,command=button_Sub)
button_mul = Button(root,text="x",padx=40,pady=20,command=button_Mul)
button_div = Button(root,text="/",padx=40,pady=20,command=button_Div)

#Print Buttons on Screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2)

button_add.grid(row=1,column=4)
button_sub.grid(row=2,column=4)
button_mul.grid(row=3,column=4)
button_div.grid(row=4,column=4)

root.mainloop()

