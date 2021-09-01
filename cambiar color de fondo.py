import tkinter as tk
import random

mywindow = tk.Tk()
def changeBG():
    #mywindow.config(background = '#76880A')"""Esto es para cambiar un solo color"""
    color = ["#76880A", "#7F8F87", "#65de4c", "#050ff4", "#78dd99", "black", "green", "cyan"]
    random_color = random.choice(color)
    mywindow.config(background = random_color)
    
mywindow.geometry("520x200")#esto es para el tamaño de la ventana
mywindow.resizable(False,False)
mywindow.title("Cambiar Color - Tkinter")
main_title = tk.Label(text = "Keury Alberto - Lendof Diaz", font = ("calibri", 12), bg = "#FFD100", fg = "black", width = "60", height = "4")
main_title.place(x = 12, y = 10)#el place es para pocisionar nuestro texto en la ventana

#Crear boton para cambiar el color de fondo
main_btn = tk.Button(mywindow, text="Cambiar color de fondo", command=changeBG)
main_btn.place(x=190, y=130) # la x es para los lados y la y para la altura

mywindow.mainloop()