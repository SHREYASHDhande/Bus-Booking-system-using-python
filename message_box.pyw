from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.Connection('operator_info')
cur=con.cursor()
root=Tk()
root.title("Tyu")
root.geometry('1200x900')
def popup():
    
        messagebox.showinfo("Error","Duplicate records not allowed")
Button3=Button(root,bg="SeaGreen1",text="click",command=popup).grid(row=6,column=5,pady=10)
