from tkinter import *
import tkinter as tk
import random

def send_data():
    Nombre_data = Nombre.get()
    apellido_data = apellido.get()
    contraseña_data =str(contraseña.get())
    años_data =str(años.get())

    print(Nombre_data, "\t", apellido_data, "\t", contraseña_data, "\t", años_data)

    #para guardar los datos en un documento

    newfile = open("Registro.txt", "a")# w y a son 2 maneras para guardar los datos 
    newfile.write(Nombre_data)
    newfile.write("\t")
    newfile.write(apellido_data)
    newfile.write("\t")
    newfile.write(contraseña_data)
    newfile.write("\t")
    newfile.write(años_data)
    newfile.write("\n") # \t es para hacer un espacio y \n es para dejar una linea poner la otra debajo
    newfile.close()
    print("Su registro ya se completo. Nombre: {} | Apellido: {} ".format(Nombre_data, apellido_data))

    #Esto aqui abajo es para cuando le demos a eviar info se borren los datos del campo
    Nombre_entry.delete(0,END)
    apellido_entry.delete(0,END)
    contraseña_entry.delete(0,END)
    años_entry.delete(0,END)

def CambioColor():
    color = ["#76880A", "#7F8F87", "#65de4c", "#050ff4", "#78dd99", "black", "green", "cyan"]
    random_color = random.choice(color)
    mywindow.config(background = random_color)


mywindow = Tk()
mywindow.geometry("650x550")
mywindow.resizable(False,False)
mywindow.config(background = "#212141")
mywindow.title("Formulario")
main_title = Label(text = "Registro De Datos | Keury Lendof", font = ("cambria", 13), bg = "#56CD63",
fg = "white", width = "550", height = "2")
main_title.pack()

Nombre_label = Label(text="Nombre", bg="#FFEEDD")
Nombre_label.place(x=22, y=70)
apellido_label = Label(text="Apellido", bg="#FFEEDD")
apellido_label.place(x=22, y=130)
contraseña_label = Label(text="Contraseña", bg="#FFEEDD")
contraseña_label.place(x=22, y=190)
años_label = Label(text="Años", bg="#FFEEDD")
años_label.place(x=22, y=250)
boton = tk.Button(mywindow, text="Cambiar color de fondo", command=CambioColor)
boton.place(x=500, y=70)


Nombre = StringVar()
apellido = StringVar()
contraseña = StringVar()
años = StringVar()

Nombre_entry = Entry(textvariable=Nombre, width="40")
apellido_entry = Entry(textvariable=apellido, width="40")
contraseña_entry = Entry(textvariable=contraseña, width="40", show="*")#el show es para que la contraseña no se vea
años_entry = Entry(textvariable=años, width="40")

Nombre_entry.place(x=22, y=100)
apellido_entry.place(x=22, y=160)
contraseña_entry.place(x=22, y=220)
años_entry.place(x=22, y=280)

submit_btn = Button(mywindow, text="Enviar Info", command=send_data, width="30", height="2", bg="#00CD63")
submit_btn.place(x=22, y=320)

mywindow.mainloop()
