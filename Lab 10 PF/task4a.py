import tkinter 
window = tkinter.Tk() 
window.title("Binding Functions")  
def say_Assalam_o_Alekum():     
    tkinter.Label(window, text = "Assalam o Alekum").pack()  
tkinter.Button(window, text = "Click Me!", command = say_Assalam_o_Alekum).pack() # 'command' is executed when you click the buttonin this above case we're calling the function 'say_Assalam_o_Alekum'. 
window.mainloop()
