import tkinter
window = tkinter.Tk()
window.title("Playing with GUI")

# creating 3 simple Labels containing some text
# sufficient widht
tkinter.Label(window, text = "Sufficient width", fg = "white", bg = "purple").pack()

# width of X
tkinter.Label(window, text = "Taking all available X width", fg = "white", bg = "green").pack(fill = "x")

# height of Y
tkinter.Label(window, text = "Taking all available Y height", fg = "white", bg = "black").pack(side = "left", fill = "y")

window.mainloop()
