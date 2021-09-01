import tkinter as tk

#crear nueva instancia

mywindow = tk.Tk()

#titulo y tamaño de la ventana

mywindow.title("Keury + Lendof")
mywindow.geometry("600x400")
mywindow.config(background = "#FF0000")
main_title = tk.Label(text = "Keury Alberto - Lendof Diaz", font = ("calibri", 14), bg = "#FFD100", fg = "black", width = "60", height = "10")
main_title.place(x = 0, y = 50)

mywindow.mainloop()

#Ventana transpalente

mywindow = tk.Tk()
mywindow.title("Ventana Transparente")
mywindow.geometry("600x400")
mywindow.resizable(False,False)
mywindow.config(background = "#3b98FA")
main_title = tk.Label(text = "Transparente", font = ("Tahoma", 14), bg = "#ff7763", fg = "black", width = "60", height = "4")
main_title.place(x = 0, y = 50)
mywindow.wm_attributes("-alpha", 0.4)#esto le da la transparencia

mywindow.mainloop()
