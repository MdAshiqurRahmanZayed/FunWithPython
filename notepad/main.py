from tkinter import *
import tkinter as tk
from tkinter.filedialog import *

#saveFile
def saveFile():
     new_file = asksaveasfile(mode='w',filetypes=[('text files','.txt')])
     if new_file is None:
          return
     text = str(entry.get(1.0,END))
     new_file.write(text)
     new_file.close()

#openFile
def openFile():
     file = askopenfile(mode='r',filetypes=[('text files','*.txt')])
     if file is not None:
          content = file.read()
     entry.insert(INSERT,content)
     
#clearFile
def clearFile():
     entry.delete(1.0,END)


#Canvas
Canvas = tk.Tk()
Canvas.geometry("600x400")
Canvas.title("Notepad")
Canvas.config(bg="white")

#frame
top = Frame(Canvas)
top.pack(padx=10,pady=5,anchor='nw')

#button
b1 = Button(Canvas,text="Open",bg="#858585",command=openFile)
b1.pack(in_=top,side=LEFT)

b2 = Button(Canvas,text="Save",bg="#858585",command=saveFile)
b2.pack(in_=top,side=LEFT)

b3 = Button(Canvas,text="Clear",bg="#858585",command=clearFile)
b3.pack(in_=top,side=LEFT)

b4 = Button(Canvas,text="Exit",bg="#858585",command=exit)
b4.pack(in_=top,side=LEFT)

#Entry
entry = Text(Canvas,wrap=WORD,bg="#F9DDA4",font=(20),fg="black")
entry.pack(padx=10,pady=5,expand=True,fill=BOTH)

Canvas.mainloop()