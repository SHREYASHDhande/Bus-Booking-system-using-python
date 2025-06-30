from tkinter import *
from tkinter import  messagebox
import sqlite3
import my_database as use
import bus_booking_system

def home_window():
    root.destroy()
    import Project_HomePage


ticket_details=bus_booking_system.read_booking()

a=ticket_details[-1]
print(ticket_details)
root=Tk()
root.title("New Bus")
root.geometry('1200x900')

    
my_image=PhotoImage(file="starbusx.png")
my_button_img=PhotoImage(file="Button.png")
my_label=Label(image=my_button_img)
frame1=Frame(root,padx=10,pady=10,bd=1)
frame1.pack()
L1=Label(frame1,image=my_image,pady=15).grid(row=1,column=2)
L2=Label(frame1,text=" Online Bus Booking system ",pady=15,bd=1,font=("ARIAL",14),bg="gold").grid(row=2,column=2)

frame=Frame(root,padx=10,pady=10,bd=1)
frame.pack()
L3=Label(frame,text=" Bus Ticket ",bd=3,font=("ARIAL",12),bg="gold").grid(row=3,column=2)

frame3=Frame(root,padx=10,pady=10,bd=1)
frame3.pack()
L1=Label(frame3,text="Passenger :"+a[5],pady=15,bd=1,font=("ARIAL",11)).grid(row=4,column=0)
L2=Label(frame3,text="Gender :"+a[6],pady=15,bd=1,font=("ARIAL",11)).grid(row=4,column=1)
L3=Label(frame3,text="Total seats :"+str(a[7]),pady=15,bd=1,font=("ARIAL",11)).grid(row=5,column=0)
L4=Label(frame3,text="Mobile :"+str(a[8]),pady=15,bd=1,font=("ARIAL",11)).grid(row=5,column=1)
L5=Label(frame3,text="Age :"+str(a[9]),pady=15,bd=1,font=("ARIAL",11)).grid(row=6,column=0)
L6=Label(frame3,text="Booking Id :"+a[0],pady=15,bd=1,font=("ARIAL",11)).grid(row=6,column=1)
L7=Label(frame3,text="Travel date :"+a[4],pady=15,bd=1,font=("ARIAL",11)).grid(row=7,column=0)
L8=Label(frame3,text="Booked on :"+a[3],pady=15,bd=1,font=("ARIAL",11)).grid(row=7,column=1)
L9=Label(frame3,text="Board at :"+a[1],pady=15,bd=1,font=("ARIAL",11)).grid(row=8,column=0)

bus_charge=bus_booking_system.show_fare(a[10])
L10=Label(frame3,text="Pay Rs. "+str(bus_charge[0])+" for each passenger at the time of boarding",pady=15,bd=1,font=("ARIAL",14)).grid(row=9,column=0,columnspan=2)
c=messagebox.showinfo("Success","You ticket is booked")
if(c=='ok'):
    root.destroy()
    import Project_HomePage
    

root.mainloop()











