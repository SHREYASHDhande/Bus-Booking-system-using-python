from tkinter import *
from tkinter import  messagebox
import sqlite3
import my_database as use
def home_window():
    root.destroy()
    import Project_HomePage
root=Tk()
root.title("New Bus")
root.geometry('1200x900')
def add_values():
    con=use.connect_database()
    cur=con.cursor()
    a=Id.get()
    b=clicked.get()
    c=Capacity.get()
    d=Fare.get()
    e=Operator_Id.get()
    f=Route_Id.get()
    cur.execute('Insert into bus values(:id,:drop,:capacity,:fare,:operator_id,:route_id)',
            {
               'id':a,
               'drop':b,
               'capacity':c,
               'fare':d,
               'operator_id':e,
               'route_id':f
            }
            )
    print_records=(a,b,c,d,e,f)        
    Id.delete(0,END)
    clicked.set("Bus type")
    Capacity.delete(0,END)
    Fare.delete(0,END)
    Operator_Id.delete(0,END)
    Route_Id.delete(0,END)
    
    Label(frame2,text=print_records).grid(row=5,columnspan=12,pady=10)
    
    con.commit()
    con.close()
def add():
    a=Id.get()
    b=clicked.get()
    c=Capacity.get()
    d=Fare.get()
    e=Operator_Id.get()
    f=Route_Id.get()
    con=use.connect_database()
    cur=con.cursor()
    
    cur.execute('select * from route where Route_Id =?',(f,))
    if not cur.fetchone():
        messagebox.showerror("Error","Route_id does not exist.")
        con.rollback()
        return 

    cur.execute('SELECT * FROM operator WHERE Operator_Id = ?',(e,))
    if not cur.fetchone():
        messagebox.showerror("Error","Operator_id does not exist.")
        con.rollback()
        return
    

    if not(a  and c and d and e and f) or b=='Bus Type':
        messagebox.showerror("Error in entry","All entries must be filled")
        return
    if (c.isnumeric()==False or d.isnumeric()==False):
        messagebox.showerror("Error in entry","Fare and capacity must be numeric")
        return
        
    
    cur.execute('Select * from bus')
    records2=cur.fetchall()
    
    for count in records2:

        if(count[0]==a):
            messagebox.showerror("Error in entry","Bus_id already exist")
            return
    print(type(b))
    add_values()
    messagebox.showinfo("Update","Entries Updated successfully")
    con.commit()
    con.close()
    
def edit():
    
    con=use.connect_database()
    cur=con.cursor()
    a=Id.get()
    b=clicked.get()
    c=Capacity.get()
    d=Fare.get()
    e=Operator_Id.get()
    f=Route_Id.get()
    
    cur.execute('select * from route where Route_Id = ?',(f,))
    if not cur.fetchone():
        messagebox.showerror("Error","Route_id does not exist.")
        con.rollback()
        return 

    cur.execute('SELECT * FROM operator WHERE Operator_Id = ?',(e,))
    if not cur.fetchone():
        messagebox.showerror("Error","Operator_id does not exist.")
        con.rollback()
        return

    if not(a and c and d  and e and f) or b=='Bus Type':
        messagebox.showerror("Error in entry","All entries must be filled")
        return
    if (c.isnumeric()==False or d.isnumeric()==False):
        messagebox.showerror("Error in entry","Fare and capacity must be numeric")
        return
    con=use.connect_database()
    cur=con.cursor()
    cur.execute('Select * from bus')
    records2=cur.fetchall()
    
    for count in records2:

        if(count[0]!=a):
            messagebox.showerror("error","Bus_id doesn't exist")
            return
    
    cur.execute(""" update operator set Bus_Id=?,Type=?,Capacity=?,Fare=?,Operator_Id=?,Route_Id=?""",(a,b,c,d,e,f))
    messagebox.showinfo("Update","Entries updated successfully")
    print_records=(a,b,c,d,e,f)
    Id.delete(0,END)
    clicked.set("Bus Type")
    Capacity.delete(0,END)
    Fare.delete(0,END)
    Operator_Id.delete(0,END)
    Route_Id.delete(0,END)
    
    Label(frame2,text=print_records).grid(row=5,columnspan=12,pady=10)
    
    con.commit()
    con.close()

    
my_image=PhotoImage(file="starbusx.png")
my_button_img=PhotoImage(file="Button.png")
my_label=Label(image=my_button_img)
frame1=Frame(root,padx=10,pady=10,bd=1)
frame1.pack()
L1=Label(frame1,image=my_image,pady=15).grid(row=1,column=2)
L2=Label(frame1,text=" Online Bus Booking system ",pady=15,bd=1,font=("Montserrat",14),bg="gold").grid(row=2,column=2)

frame=Frame(root,padx=10,pady=10,bd=1)
frame.pack()
L3=Label(frame,text=" Add Bus Details ",bd=3,font=("Montserrat",12),bg="gold").grid(row=3,column=2)

frame2=Frame(root)
frame2.pack(pady=30)

Label1=Label(frame2,text="Bus Id",font=("Montserrat",9)).grid(row=4,column=0)
Id=Entry(frame2)
Id.grid(row=4,column=1,padx=10)

clicked=StringVar()
drop=OptionMenu(frame2,clicked,"AC 2X2","AC 3X2","Non AC 2X2","Non AC 3X2","AC-Sleeper 2X1","Non AC-Sleeper 2X1")
clicked.set("Bus Type")
# We can also pass a variable named 'option' of all days and in OptionMenu(root,clicked,*option)

Label2=Label(frame2,text="Bus Type",font=("Montserrat",9)).grid(row=4,column=2)
drop.grid(row=4,column=3)

Label3=Label(frame2,text="Capacity",font=("Montserrat",9)).grid(row=4,column=4)
Capacity=Entry(frame2)
Capacity.grid(row=4,column=5,padx=10)

Label2=Label(frame2,text="Fare Rs",font=("Montserrat",9)).grid(row=4,column=6)
Fare=Entry(frame2)
Fare.grid(row=4,column=7,padx=10)

Label3=Label(frame2,text="Operator ID",font=("Montserrat",9)).grid(row=4,column=8)
Operator_Id=Entry(frame2)
Operator_Id.grid(row=4,column=9,padx=10)

Label3=Label(frame2,text="Route ID",font=("Montserrat",9)).grid(row=4,column=10)
Route_Id=Entry(frame2)
Route_Id.grid(row=4,column=11,padx=11)

frame_my=Frame(root)
frame_my.pack(pady=30)
Button1=Button(frame_my,text="Add",bg="bisque",font=("Montserrat",11,'bold'),command=add).grid(row=6,column=4,padx=10,pady=15)
Button2=Button(frame_my,text="Edit",bg="bisque",font=("Montserrat",11,'bold'),command=edit).grid(row=6,column=5,padx=10,pady=15)
Button3=Button(frame_my,bg="SeaGreen1",image=my_button_img,command=home_window).grid(row=6,column=6,padx=10,pady=15)




