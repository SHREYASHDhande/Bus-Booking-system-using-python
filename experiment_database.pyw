from tkinter import *
import sqlite3
con=sqlite3.connect('exp_info')
cur=con.cursor()
root=Tk()
root.title("exp")
root.geometry('1200x900')
##cur.execute('''
##    create table if not exists experiment(
##        operator_id int
##    )
##    ''')
def submit():
    con=sqlite3.connect('exp_info')
    cur=con.cursor()
    a=Id.get()
    
    cur.execute('Insert into experiment values(:id)',
    {
       'id':a,
       
    }
    )
    Id.delete(0,END)
    
    cur.execute('Select * from experiment')
    records=cur.fetchall()
    print(records)
    print_records=''
    for record in records[0]:
        print_records+=str(record)+',' 
    Label(root,text=print_records).grid(row=5,columnspan=12,pady=10)
    con.commit()
    con.close()
def edit():
    con=sqlite3.Connection('exp_info')
    cur=con.cursor()
    
    cur.execute('Select * from experiment ')
    records=cur.fetchall()
    print(records)
Button1=Button(root,text="Edit",bg="bisque",font=("Montserrat",9,'bold'),command=edit).grid(row=2,column=1,padx=10)
Button2=Button(root,text="Add",bg="bisque",font=("Montserrat",9,'bold'),command=submit).grid(row=2,column=0,padx=10)
Label1=Label(root,text="Operator Id",font=("Montserrat",9)).grid(row=0,column=0)
Id=Entry(root)
Id.grid(row=1,column=1,padx=10)
