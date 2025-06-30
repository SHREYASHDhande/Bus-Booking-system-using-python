

from tkinter import *
root=Tk()
root.geometry ('350x300')
Label(root, text='Select the day of the week').grid(row = 0, column = 0)
v1=StringVar()
v1.set("Click to Select")
option =["Monday","Tuesday", "Wednesday", "Thursday","Friday","Saturday","Sunday"]
OptionMenu(root,v1,*option).grid(row=1, column=0)
def fun():
       Label(root,text=v1.get()).grid(row=3, column=1)
Button (root,text=' Show Choice', command=fun).grid(row=2, column=1)
root.mainloop()
