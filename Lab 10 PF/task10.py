import tkinter 
import tkinter 
window = tkinter.Tk() 
window.title("Image or Logo on GUI") 
icon = tkinter.PhotoImage(file = "uitlogo.jpg") 
label = tkinter.Label(window, image = icon) 
label.pack()  

window.mainloop() 
