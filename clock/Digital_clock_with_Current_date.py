from tkinter import font
from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import date



root = Tk()
root.title("Clock")
today = date.today()

def time():
     string = strftime('%H:%M:%S %p\n')
     lebel.config(text=string)
     lebel.after(1000,time)
lebel  = Label(root,font=("ds-digital",80), background="black",foreground="cyan")
lebel.pack()

time()
mainloop()


