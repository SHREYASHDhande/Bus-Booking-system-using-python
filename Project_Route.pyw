from tkinter import *
from tkinter import messagebox
import my_database as use
root=Tk()
root.title("Tyu")
root.geometry('1200x900')

def home_window():
    root.destroy()
    import Project_HomePage
def add_values():
    con=use.connect_database()
    cur=con.cursor()
    a=RId.get()
    b=SName.get()
    c=SId.get()
    
    cur.execute('Insert into route values(:id,:name,:sid)',
            {
               'id':a,
               'name':b,
               'sid':c,
               
            }
            )
    print_records=(a,b,c)        
    RId.delete(0,END)
    SName.delete(0,END)
    SId.delete(0,END)
    
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
    a=RId.get()
    b=SName.get()
    c=SId.get()

    if not(a and b and c ):
        messagebox.showerror("Error in entry","All entries must be filled")
        return
    
        
    con=use.connect_database()
    cur=con.cursor()
    cur.execute('Select * from route')
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
    
    a=RId.get()
    b=SName.get()
    c=SId.get()
    
    if not(a and b and c ):
        messagebox.showerror("Error","All entries must be filled")
        return
    
    con=use.connect_database()
    cur=con.cursor()
    cur.execute("""Select * from route where Route_Id=? and Station_Name=? """,(a,b))
    records2=cur.fetchall()
    print_records=(a,b,c)
    
    var=0
    
    cur.execute(""" delete from route where Route_Id=? and Station_Name=?""",(a,b))    
    Label(frame2,text="").grid(row=5,columnspan=12,pady=10)
        
            
    
    
    RId.delete(0,END)
    SName.delete(0,END)
    SId.delete(0,END)
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

Label1=Label(frame2,text="Route ID",font=("ARIAL",9)).grid(row=4,column=0)
RId=Entry(frame2)
RId.grid(row=4,column=1,padx=10)

Label2=Label(frame2,text="Station Name",font=("ARIAL",9)).grid(row=4,column=2)
SName=Entry(frame2)
SName.grid(row=4,column=3,padx=10)

Label3=Label(frame2,text="Station ID",font=("ARIAL",9)).grid(row=4,column=4)
SId=Entry(frame2)
SId.grid(row=4,column=5,padx=10)

Button1=Button(frame2,text="Add Route",bg="LIGHT GREEN ",font=("ARIAL",11,'bold'),command=add).grid(row=4,column=6,padx=10,pady=15)
Button2=Button(frame2,text="Delete Route ",bg="LIGHT GREEN ",font=("ARIAL",11,'bold'),command=delete).grid(row=4,column=7,padx=10,pady=15)
Button3=Button(frame2,bg="SeaGreen1",image=my_button_img,command=home_window).grid(row=6,column=4,padx=10,pady=15)




