import tkinter as tk
from tkinter import messagebox

mywindow = tk.Tk()
mywindow.geometry("500x300")
mywindow.title("Keury Lendof")
mywindow.resizable(False,False)

def myMessage():
    messagebox.showwarning("Dangerous!", "MMG va a explotar la computadura! ")
    
btn1 = tk.Button(mywindow, text="1st Button", command= myMessage)#command es para invocar la funcion que uno desee
btn1.pack()

mywindow.mainloop()