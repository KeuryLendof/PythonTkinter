#Esta parte solo muestra la hora y ya
"""import tkinter
from time import strftime

root = tkinter.Tk()
root.title("Reloj Digital")
myClock = tkinter.Label()
myClock.pack()
myClock['font'] = 'Tahoma 150 bold'

strftime(' %H:%M:%S')

def tic():
    myClock['text'] = strftime(' %H:%M:%S')
tic()

#Esta parte hace que el reloj se mueva a cada mil mili segundos

def tac():
    tic()
    myClock.after(1000, tac)
tac()

myClock['fg'] = 'black'
#myClock['fg'] = 'white'
myClock['bg'] = '#2ffbf0'
#myClock['bg'] = '#af25f0'

myClock.mainloop() """



import time
import tkinter as tk
import datetime
from datetime import date

class Digital_clock():
    def __init__(self):
        self.mywindow = tk.Tk()
        self.mywindow.geometry("600x380")
        self.mywindow.resizable(0,0) #para que la ventana no se pueda agrandar
        self.mywindow.title("Reloj Digital | Python + Tkinter")
        self.mywindow.config(background='#1f2f3f')
        self.current_time_label = tk.Label(text="",font=('tahoma', 44), fg='#ffffff', bg='#72a922', pady=10, padx=10)
        self.week_day_label = tk.Label(text="", font=('tahoma', 12), fg='#ffffff', bg='#449a66', pady=10, padx=10)
        self.created_by_label = tk.Label(text="Keury Lendof", font=('tahoma', 11), fg='#ffffff', bg='#ff3333', pady=7, padx=7) # los pad son para el tamaño
        self.current_time_label.place(x=175, y=50) #el place es para posicional nuestra etiqueta en nuestra ventana
        self.week_day_label.place(x=210, y=160)
        self.created_by_label.place(x=250, y=220)
        self.update_clock()
        self.get_date() #para poder mostrarlo debemos de invocar la aqui
        self.mywindow.mainloop()
    
    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.current_time_label.configure(text=now)
        self.mywindow.after(1000, self.update_clock)

    def get_date(self):
        datetime_object = datetime.datetime.now()
        week_day = datetime_object.strftime("%A")

        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        self.week_day_label.configure(text=d1 + ' | ' + week_day)

main = Digital_clock()
