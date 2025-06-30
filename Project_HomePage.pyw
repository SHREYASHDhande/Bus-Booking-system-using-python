from tkinter import *
root=Tk()
root.title("Home Page")
root.geometry('1200x900')
my_image=PhotoImage(file="starbusx.png")


def fun1():
    root.destroy()
    import Project_BusBook
    
def fun2():
    root.destroy()
    import Project_BookedSeat
    
    
def fun3():
    root.destroy()
    import Project_BusDetails
    
    
    
frame1=Frame(root,padx=10,pady=10,bd=1)
frame1.pack()
L1=Label(frame1,image=my_image,pady=30).grid(row=1,column=2)
L2=Label(frame1,text=" Online Bus Booking system ",pady=30,bd=3,font=("ARIAL",28),bg="gold").grid(row=2,column=2)

frame2=Frame(root)
frame2.pack(pady=30)
Button1=Button(frame2,text="Seat Booking",command=fun1,bg="LIGHT GREEN",font=("ARIAL",15,'bold')).grid(row=3,column=1,padx=15,pady=15)
Button2=Button(frame2,text="Check Booked Status",command=fun2,bg="LIGHT GREEN",font=("ARIAL",15,'bold')).grid(row=3,column=2,padx=15,pady=15)
Button3=Button(frame2,command=fun3,text="Add Bus Details",bg="LIGHT GREEN",font=("ARIAL",15,'bold')).grid(row=3,column=3,padx=15,pady=15)
Label(frame2,text="For Admins only",bg="LIGHT GREEN",fg="red",font=("ARIAL",10,'bold')).grid(row=4,column=3,padx=8,pady=8)

