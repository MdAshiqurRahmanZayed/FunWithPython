from cgitb import text
from curses import window
import tkinter as tk 
from pytube import YouTube

window = tk.Tk()
window.geometry("700x800")
window.config(bg="#3b3e50")
window.resizable(width=False,height=False)
window.title("Youtube video downloader")


#Main Function
def Download_Video():     
    YouTube(link.get()).streams.get_highest_resolution().download()
    
    # video.download()
    tk.Label(window, text = 'Your Video is downloaded!', font = 'arial 15',fg="White",bg="#EC7063").place(x= 10 , y = 140)  


# Adding Widgets to Tkinter Screen
link = tk.StringVar()
tk.Label(window, text="Youtube video downloader", width=50,bg="Black", fg="White", font="arial 20 bold").pack()
tk.Label(window, text="Paste your code here", fg="White",bg="#3b3e50", width=20,font="arial 20 bold").place(x=5,y=60)
link_enter = tk.Entry(window,width=50,textvariable=link,font="arial 15 bold",bg="lightgreen").place(x=5,y=100)
tk.Button(window,text="Download Video",font = 'arial 15 bold' ,fg="white",bg = 'black', padx = 2,command=Download_Video).place(x=385 ,y = 140)



window.mainloop()