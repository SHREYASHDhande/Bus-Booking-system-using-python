from tkinter import *
from tkinter import  messagebox 
import sqlite3
import my_database as use

root=Tk()
root.title("New operator")
root.geometry('1200x900')
def home_window():
    root.destroy()
    import Project_HomePage
def add_values():
    con=use.connect_database()
    cur=con.cursor()
    a=Id.get()
    b=Name.get()
    c=Address.get()
    d=Phone.get()
    e=Email.get()
    cur.execute('Insert into operator values(:id,:name,:address,:phone,:email)',
            {
               'id':a,
               'name':b,
               'address':c,
               'phone':d,
               'email':e
            }
            )
    print_records=(a,b,c,d,e)        
    Id.delete(0,END)
    Name.delete(0,END)
    Address.delete(0,END)
    Phone.delete(0,END)
    Email.delete(0,END)
    
    Label(frame2,text=print_records).grid(row=5,columnspan=12,pady=10)
    
    con.commit()
    con.close()    
  
##    cur.execute('Select * from ')
##    records=cur.fetchall()
##    print(records)
##    print_records=''
##    
##    for record in records:
##        print_records+=str(record)+','
##    Label(frame2,text=print_records).grid(row=5,columnspan=12,pady=10)
    
    

def add():
    a=Id.get()
    b=Name.get()
    c=Address.get()
    d=Phone.get()
    e=Email.get()

    if not(a and b and c and d and e):
        messagebox.showerror("Error in entry","All entries must be filled")
        return
    if (len(d)!=10 or d.isnumeric()==False):
        messagebox.showerror("Error in entry","Phone no. must be 10 digit and numeric")
        return
        
    con=use.connect_database()
    cur=con.cursor()
    cur.execute('Select * from operator')
    records2=cur.fetchall()
    
    for count in records2:

        if(count[0]==a):
            messagebox.showerror("Error in entry","operator_id already exist")
            return
    
    add_values()
    messagebox.showinfo("Update","Entries added successfully")
    con.commit()
    con.close()
    
def edit():
    
    
    a=Id.get()
    b=Name.get()
    c=Address.get()
    d=Phone.get()
    e=Email.get()
    if not(a and b and c and d and e):
        messagebox.showerror("error","All entries must be filled")
        return
    if (len(d)!=10 or d.isnumeric()==False):
        messagebox.showerror("Error in entry","Phone no. must be 10 digit and numeric")
        return
    con=use.connect_database()
    cur=con.cursor()
    cur.execute('Select * from operator')
    records2=cur.fetchall()
    
    for count in records2:

        if(count[0]!=a):
            messagebox.showerror("error","operator_id doesn't exist")
            return
    cur.execute(""" update operator set Operator_Id=?,Name=?,Address=?,Phone=?,Email=?""",(a,b,c,d,e))
    messagebox.showinfo("Update","Entries updated successfully")
    Id.delete(0,END)
    Name.delete(0,END)
    Address.delete(0,END)
    Phone.delete(0,END)
    Email.delete(0,END)
    print_records=(a,b,c,d,e)
    Label(frame2,text=print_records).grid(row=5,columnspan=12,pady=10)
    con.commit()
    con.close()
        
##    for count in records2:
##        if(records1[0]!=count[0]):
##            messagebox.showerror("Error","Operator_id does not exist")
##            return 
##        else:
##            operator_data=(a,b,c,d,e)
##            cur1.execute('update   set Operator_ID=?, Name =?, Address=?,Phone=?,Email=?',(*operator_data,))
##
##            messagebox.showinfo("yes","successfully edited")
##            
##    Id.delete(0,END)
##    Name.delete(0,END)
##    Address.delete(0,END)
##    Phone.delete(0,END)
##    Email.delete(0,END)
            
        
        
        
    
                
    
my_image=PhotoImage(file="starbusx.png")
my_button_img=PhotoImage(file="Button.png")
my_label=Label(image=my_button_img)
frame1=Frame(root,padx=10,pady=10,bd=1)
frame1.pack()
L1=Label(frame1,image=my_image,pady=15).grid(row=1,column=2)
L2=Label(frame1,text=" Online Bus Booking system ",pady=15,bd=1,font=("Montserrat",14),bg="gold").grid(row=2,column=2)

frame=Frame(root,padx=10,pady=10,bd=1)
frame.pack()
L3=Label(frame,text=" Add Bus Operator Details ",bd=3,font=("Montserrat",12),bg="gold").grid(row=3,column=2)

frame2=Frame(root)
frame2.pack(pady=30)
Label1=Label(frame2,text="Operator Id",font=("Montserrat",9)).grid(row=4,column=0)
Id=Entry(frame2)
Id.grid(row=4,column=1,padx=10)

Label2=Label(frame2,text="Name",font=("Montserrat",9)).grid(row=4,column=2)
Name=Entry(frame2)
Name.grid(row=4,column=3,padx=10)

Label3=Label(frame2,text="Address",font=("Montserrat",9)).grid(row=4,column=4)
Address=Entry(frame2)
Address.grid(row=4,column=5,padx=10)

Label2=Label(frame2,text="Phone",font=("Montserrat",9)).grid(row=4,column=6)
Phone=Entry(frame2)
Phone.grid(row=4,column=7,padx=10)

Label3=Label(frame2,text="Email",font=("Montserrat",9)).grid(row=4,column=8)
Email=Entry(frame2)
Email.grid(row=4,column=9,padx=10)

Button1=Button(frame2,text="Add",bg="bisque",font=("Montserrat",9,'bold'),command=add).grid(row=4,column=10,padx=10)
Button2=Button(frame2,text="Edit",bg="bisque",font=("Montserrat",9,'bold'),command=edit).grid(row=4,column=11,padx=10)
Button3=Button(frame2,bg="SeaGreen1",image=my_button_img,command=home_window).grid(row=6,column=5,pady=10)




