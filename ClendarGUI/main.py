
from tkinter import *
import tkinter as tk

import calendar
def showCalender():
    gui = Tk()
    gui.config(background='#C2EDCE')
    gui.title("Calender for the year")
    gui.geometry("950x900")
    year =  int(myEntry.get())
    gui_content=  calendar.calendar(year)
    calYear = Label(gui,bg='#C2EDCE',fg="black", text= gui_content, font= "Consolas 15 bold")
    #calYear.grid(row=5, column=1,padx=20)
    calYear.pack()
    gui.mainloop()
    
if __name__=='__main__':

     window = Tk()
     window.title("List")
     window.geometry("700x450")
     window.configure(bg="orange red")
     
     #center this label
     cal = Label(window, text="Calender", bg="orange red", fg="white", font="none 24 bold")
     cal.config(anchor=CENTER)
     cal.pack()
     
     
     year = Label (window, text="Enter year", bg="orange red", fg="white", font="none 12 bold")
     year.config(anchor=CENTER)
     year.pack()
     
     myEntry = tk.Entry(window, width=40)
     myEntry.pack(pady=20)

     btn = tk.Button(window, height=1, width=10, text="Show Calender", command=showCalender)
     btn.pack()
     
     Exit = Button(window, text='Exit', fg='Black', bg='blue', command=exit)
     Exit.config(anchor=CENTER)
     Exit.pack()
     
     window.mainloop()