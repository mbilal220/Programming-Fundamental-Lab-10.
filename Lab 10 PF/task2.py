import tkinter
window = tkinter.Tk()
window.title("Two frames with Widgets")

top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

btnl = tkinter.Button(top_frame, text = "Butoon1", fg = "red").pack()

btn2 = tkinter.Button(top_frame, text = "Butoon2", fg = "green").pack()

btn3 = tkinter.Button(button_frame, text = "Butoon3", fg = "purple").pack(bside = "left")

btn4 = tkinter.Button(button_frame, text = "Butoon4", fg = "orange").pack(side = "left")

window.mainloop()
