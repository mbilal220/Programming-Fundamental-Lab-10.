import tkinter
window=tkinter.Tk()
window.title('Calculator')
window.resizable(0,0)
window.geometry("312x324")
input_text = tkinter.StringVar()
expr=""
def btn_clear():
    global input_text
    global expr
    input_text.set('')
    expr = ""
    print('input_text = ',input_text)
    print('expr =',expr)
    
def btn_click(item):
    
    global input_text
    global expr

    expr=expr+str(item)
    input_text.set(expr)
    print('input_text = ',input_text)
    print('expr =',expr)
def btn_equal():
    
    global input_text
    global expr
    
    res=str(input('expr'))
    input_text.set(res)
    expr = ''
    
    print('input_text = ',input_text)
    print('expr =',expr)
    
input_frame=tkinter.Frame(window,width=312,height=50,bd=0,highlightbackground='black',highlightcolor='black',highlightthickness=1)
input_frame.pack(side="top")

input_field=tkinter.Entry(input_frame,font=('arial',18,'bold'),textvariable=input_text,width=50,justify="right",bg='white',fg='grey')
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

btn_frame=tkinter.Frame(window,width=312,height=272.5,bg='grey')
btn_frame.pack()
#row 1
clear=tkinter.Button(btn_frame,text='C',width=32,height=3,bd=0,cursor='hand2',command = lambda : btn_clear())
clear.grid(row=0,column=0,columnspan=3,padx=1,pady=1)

divide=tkinter.Button(btn_frame,text='/',width=10,height=3,bd=0,cursor='hand2',command=lambda : btn_click('/'))
divide.grid(row=0,column=3,columnspan=3,padx=1,pady=1)

#row 2

seven = tkinter.Button(btn_frame, text = "7",width = 10,height = 3, bd = 0, cursor = "hand2", command =lambda : btn_click(7))
seven.grid(row = 1, column = 0, padx = 1, pady = 1)

eight = tkinter.Button(btn_frame, text = "8", width = 10,height = 3, bd = 0, cursor = "hand2", command =lambda : btn_click(8))
eight.grid(row = 1, column = 1, padx = 1, pady = 1)

nine = tkinter.Button(btn_frame, text = "9", width = 10, height= 3, bd = 0,  cursor = "hand2", command = lambda :btn_click(9))
nine.grid(row = 1, column = 2, padx = 1, pady = 1)

multiply = tkinter.Button(btn_frame, text = "*",width = 10,height = 3, bd = 0, cursor = "hand2", command =lambda : btn_click("*"))
multiply.grid(row = 1, column = 3, padx = 1, pady = 1)

# third row
four = tkinter.Button(btn_frame, text = "4", width = 10, height= 3, bd = 0, cursor = "hand2", command = lambda :btn_click(4))
four.grid(row = 2, column = 0, padx = 1, pady = 1)
five = tkinter.Button(btn_frame, text = "5", width = 10, height= 3, bd = 0, cursor = "hand2", command =lambda : btn_click(5))
five.grid(row = 2, column = 1, padx = 1, pady = 1)
six = tkinter.Button(btn_frame, text = "6", width = 10, height= 3, bd = 0,  cursor = "hand2", command = lambda :btn_click(6))
six.grid(row = 2, column = 2, padx = 1, pady = 1)
minus = tkinter.Button(btn_frame, text = "-", width = 10,height = 3, bd = 0,  cursor = "hand2", command =lambda :btn_click("-"))
minus.grid(row = 2, column = 3, padx = 1, pady = 1)

# fourth row
one = tkinter.Button(btn_frame, text = "1",  width = 10, height= 3, bd = 0,  cursor = "hand2", command =lambda : btn_click(1))
one.grid(row = 3, column = 0, padx = 1, pady = 1)
two = tkinter.Button(btn_frame, text = "2",  width = 10, height= 3, bd = 0, cursor = "hand2", command =lambda : btn_click(2))
two.grid(row = 3, column = 1, padx = 1, pady = 1)
three = tkinter.Button(btn_frame, text = "3",  width = 10,height = 3, bd = 0,  cursor = "hand2", command =lambda : btn_click(3))
three.grid(row = 3, column = 2, padx = 1, pady = 1)
plus = tkinter.Button(btn_frame, text = "+",  width = 10, height= 3, bd = 0,  cursor = "hand2",command = lambda :btn_click("+"))
plus.grid(row = 3, column = 3, padx = 1, pady = 1)

#fifth row 
zero=tkinter.Button(btn_frame,text='0',width=10,height=3,bd=0,cursor='hand2',command=lambda :btn_click(0))
zero.grid(row=4,column=0,columnspan=2,padx=0.5,pady=0.5)
point=tkinter.Button(btn_frame,text='.',width=10,height=3,bd=0,cursor='hand2',command=lambda :btn_click('.'))
point.grid(row=4,column=2,columnspan=1,padx=1,pady=1)
equal=tkinter.Button(btn_frame,text='=',width=10,height=3,bd=0,cursor='hand2',command=lambda :btn_click('='))
equal.grid(row=4,column=3,columnspan=1,padx=1,pady=1)

window.mainloop() 
