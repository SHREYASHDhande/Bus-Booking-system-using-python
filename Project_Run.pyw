from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("New Run")
root.geometry('1200x900')
import my_database as use
def home_window():
    root.destroy()
    import Project_HomePage
    
def add_values():
    con=use.connect_database()
    cur=con.cursor()
    a=BId.get()
    b=Rdate.get()
    c=Seat_Available.get()
    
    cur.execute('Insert into run values(:id,:date,:seat)',
            {
               'id':a,
               'date':b,
               'seat':c,
               
            }
            )
    print_records=(a,b,c)        
    BId.delete(0,END)
    Rdate.delete(0,END)
    Seat_Available.delete(0,END)
    
    
    Label(frame2,text=print_records).grid(row=5,columnspan=12,pady=10)
    
    con.commit()
    con.close()    

    
    

def add():
    a=BId.get()
    b=Rdate.get()
    c=Seat_Available.get()
    
    if not(a and b and c ):
        messagebox.showerror("Error in entry","All entries must be filled")
        return
    
        
    con=use.connect_database()
    cur=con.cursor()
    cur.execute('Select * from run')
    records2=cur.fetchall()
    
    for count in records2:

        if(count[0]==a and count[1]==b):
            messagebox.showerror("Error in entry","Record already exist")
            return
    
    add_values()
    messagebox.showinfo("Update","Entries added successfully")
    con.commit()
    con.close()
    
def delete():
    
    a=BId.get()
    b=Rdate.get()
    c=Seat_Available.get()
    
    if not(a and b and c ):
        messagebox.showerror("Error","All entries must be filled")
        return
    
    con=use.connect_database()
    cur=con.cursor()
    cur.execute("""Select * from run where Bus_Id=? and Running_Date=? """,(a,b))
    records2=cur.fetchall()
    if records2 is None:
        messagebox.showerror("Delete","Record not found")
        return
    print_records=(a,b,c)
    
    
    for count in records2:

        if(count[0]!=a and count[1]!=b):
            messagebox.showerror("Error in entry","Record doesn't exist")
            return
    
    cur.execute(""" delete from route where Route_Id=? and Station_Name=?""",(a,b))
    messagebox.showinfo("Update","Entries deleted successfully")
    Label(frame2,text="").grid(row=5,columnspan=12,pady=10)
        
            
    
    
    BId.delete(0,END)
    Rdate.delete(0,END)
    Seat_Available.delete(0,END)
    print_records=(a,b,c)
    
    
    con.commit()
    con.close()

my_image=PhotoImage(file="starbusx.png")
my_button_img=PhotoImage(file="Button.png")
my_label=Label(image=my_button_img)
frame1=Frame(root,padx=10,pady=10,bd=1)
frame1.pack()
L1=Label(frame1,image=my_image,pady=15).grid(row=1,column=2)
L2=Label(frame1,text=" Online Bus Booking system ",pady=15,bd=1,font=("ARIAL",14),bg="gold").grid(row=2,column=2)

frame=Frame(root,padx=10,pady=10,bd=1)
frame.pack()
L3=Label(frame,text=" Add Bus Details ",bd=3,font=("ARIAL",12),bg="gold").grid(row=3,column=2)

frame2=Frame(root)
frame2.pack(pady=30)
Label1=Label(frame2,text="Bus ID",font=("ARIAL",9)).grid(row=4,column=0)
BId=Entry(frame2)
BId.grid(row=4,column=1,padx=10)

Label2=Label(frame2,text="Running Date",font=("ARIAL",9)).grid(row=4,column=2)
Rdate=Entry(frame2)
Rdate.grid(row=4,column=3,padx=10)

Label3=Label(frame2,text="Seat Available",font=("ARIAL",9)).grid(row=4,column=4)
Seat_Available=Entry(frame2)
Seat_Available.grid(row=4,column=5,padx=10)

Button1=Button(frame2,text="Add Run",bg="bisque",font=("ARIAL",11,'bold'),command=add).grid(row=4,column=6,padx=10,pady=15)
Button2=Button(frame2,text="Delete Run ",bg="bisque",font=("ARIAL",11,'bold'),command=delete).grid(row=4,column=7,padx=10,pady=15)
Button3=Button(frame2,bg="SeaGreen1",image=my_button_img,command=home_window).grid(row=6,column=4,padx=10,pady=15)




