import tkinter 
class MyGUI: 
    def __init__(self, window): 
        self.text_btn = tkinter.Button(window, text = "Click Me!", command = self.say_greetings)  
        self.text_btn.pack() 
        self.close_btn = tkinter.Button(window, text = "Close", command = window.quit)  
        self.close_btn.pack() 
    def say_greetings(self): 
        tkinter.Label(window, text = "Welcome to Usman Institute of Technology").pack() 
window = tkinter.Tk() 
window.title("GUI with Class Concept") 
my_gui = MyGUI(window) 
window.mainloop()
