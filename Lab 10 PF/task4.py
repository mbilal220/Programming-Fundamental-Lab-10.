import tkinter
window = tkinter.Tk()
window.title("My Login Window")

tkinter.Label(window, text = "Username").grid(row = 0)

tkinter.Entry(window).grid(row = 0, column = 1)

tkinter.Label(window, text = "Password").grid(row = 1)

tkinter.Entry(window).grid(row = 1, column = 1)

tkinter.Checkbutton(window, text = "Keep me loged In").grid(columnspan = 2)
window.mainloop()
