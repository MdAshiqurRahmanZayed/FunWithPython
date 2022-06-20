from tkinter import *

root  = Tk()

#Text Input Area
main = Entry(root,width=35,borderwidth=5)
main.grid(row=0,column=0,columnspan=3,padx=3)

list_of_number = []
#Function
def numberInput(number):
     current_value = main.get()
     main.delete(0,END)
     main.insert(0, str(current_value)+str(number))

def clear_values():
     list_of_number.clear()
     main.delete(0,END)

def sum_of_value():
     num1 = main.get()
     list_of_number.append(num1)
     main.delete(0,END)



def equals():
     num1 = main.get()
     list_of_number.append(int(num1))
     main.delete(0,END)
     
     sum = 0
     for values in list_of_number:
          sum+=int(values)
     main.insert(0,sum)
          
     

#Button

button9 = Button(root,text="9",padx=40,pady=20,command=lambda:numberInput(9)).grid(row=1 , column=0)
button8 = Button(root,text="8",padx=40,pady=20,command=lambda:numberInput(8)).grid(row= 1, column=1)
button7 = Button(root,text="7",padx=40,pady=20,command=lambda:numberInput(7)).grid(row=1 , column=2)

button6 = Button(root,text="6",padx=40,pady=20,command=lambda:numberInput(6)).grid(row=2 , column=0)
button5 = Button(root,text="5",padx=40,pady=20,command=lambda:numberInput(5)).grid(row= 2, column=1)
button4 = Button(root,text="4",padx=40,pady=20,command=lambda:numberInput(4)).grid(row= 2, column=2)

button3 = Button(root,text="3",padx=40,pady=20,command=lambda:numberInput(3)).grid(row= 3, column=0)
button2 = Button(root,text="2",padx=40,pady=20,command=lambda:numberInput(2)).grid(row= 3, column=1)
button1 = Button(root,text="1",padx=40,pady=20,command=lambda:numberInput(1)).grid(row=3 , column=2)

button0 = Button(root,text="0",padx=40,pady=20,command=lambda:numberInput(0)).grid(row=4 , column=0)


button_add = Button(root, text="+", padx=40, pady=20, command=sum_of_value).grid(row=4, column=1)
button_clear = Button(root, text="clear", padx=40, pady=20, command=clear_values).grid(row=4, column=2)
button_equals = Button(root, text="equals", padx=40, pady=20, command=equals).grid(row=5, column=1,columnspan=2)

root.mainloop()
