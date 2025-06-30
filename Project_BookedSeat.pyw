from tkinter import *
from tkinter import messagebox
import bus_booking_system
import my_database
root=Tk()
root.title("Tyu")
root.geometry('1200x900')
my_image=PhotoImage(file="starbusx.png")
global c
def search():
    
    a=Search.get()
    if not a:
        
        messagebox.showerror("Error in entry","Enter mobile number")
        return
    
    if (len(a)!=10 or a.isnumeric()==False):
        messagebox.showerror("Error in entry","Phone no. must be 10 digit and numeric")
        return
   
    ticket_details=bus_booking_system.show_tickets_from_mobile(a)
    print(ticket_details)
    
    if not ticket_details :
        
        y=messagebox.askyesno("No record","No record found Do you want to book now ?")
        if y==1:
            root.destroy()
            import Project_BusBook
    else:
        c=ticket_details[0]
        frame3=Frame(root,padx=10,pady=10,bd=1)
        frame3.pack()
        
        L1=Label(frame3,text="Passenger :"+c[5],pady=15,bd=1,font=("Montserrat",11)).grid(row=4,column=0)
        L2=Label(frame3,text="Gender :"+c[6],pady=15,bd=1,font=("Montserrat",11)).grid(row=4,column=1)
        L3=Label(frame3,text="Total seats :"+str(c[7]),pady=15,bd=1,font=("Montserrat",11)).grid(row=5,column=0)
        L4=Label(frame3,text="Mobile :"+str(c[8]),pady=15,bd=1,font=("Montserrat",11)).grid(row=5,column=1)
        L5=Label(frame3,text="Age :"+str(c[9]),pady=15,bd=1,font=("Montserrat",11)).grid(row=6,column=0)
        L6=Label(frame3,text="Booking Id :"+c[0],pady=15,bd=1,font=("Montserrat",11)).grid(row=6,column=1)
        L7=Label(frame3,text="Travel date :"+c[4],pady=15,bd=1,font=("Montserrat",11)).grid(row=7,column=0)
        L8=Label(frame3,text="Booked on :"+c[3],pady=15,bd=1,font=("Montserrat",11)).grid(row=7,column=1)
        L9=Label(frame3,text="Board at :"+c[1],pady=15,bd=1,font=("Montserrat",11)).grid(row=8,column=0)


         
    




        
        
        
    
    




frame1=Frame(root,padx=10,pady=10,bd=1)
frame1.pack()
L1=Label(frame1,image=my_image,pady=15).grid(row=1,column=2)
L2=Label(frame1,text=" Check Your Bus Booking  ",pady=15,bd=1,font=("Montserrat",14),bg="gold").grid(row=2,column=2)

frame=Frame(root,padx=10,pady=10,bd=1)
frame.pack()
L3=Label(frame,text=" Enter Your Mobile No: ",font=("Montserrat",10)).grid(row=3,column=0)
Search=Entry(frame)
Search.grid(row=3,column=1,padx=10)
Button1=Button(frame,text="Check Status",bg="bisque",font=("Montserrat",10,'bold'),command=search).grid(row=3,column=2,padx=10)




