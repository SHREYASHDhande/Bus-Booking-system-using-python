from tkinter import *
root=Tk()
root.title("Tyu")
root.geometry('1200x900')
my_image=PhotoImage(file="starbusx.png")

def fun1():
    root.destroy()
    import Project_operator
    
def fun2():
    root.destroy()
    import Project_NewBus
    
    
def fun3():
    root.destroy()
    import Project_Route
def fun4():
    root.destroy()
    import Project_Run
    

    
    
frame1=Frame(root,padx=10,pady=10,bd=1)
frame1.pack()
L1=Label(frame1,image=my_image,pady=20).grid(row=1,column=2)
L2=Label(frame1,text=" Online Bus Booking system ",pady=20,bd=1,font=("Montserrat",14),bg="gold").grid(row=2,column=2)

frame=Frame(root,padx=10,pady=15,bd=1)
frame.pack()
L3=Label(frame,text=" Add New Details to Database ",bd=1,font=("Montserrat",12),bg="gold").grid(row=3,column=2)

frame2=Frame(root)
frame2.pack(pady=30)
Button1=Button(frame2,text="New Operator",command=fun1,bg="bisque",font=("Montserrat",11,'bold')).grid(row=4,column=0,padx=15,pady=15)
Button2=Button(frame2,text="New Bus",command=fun2,bg="coral",font=("Montserrat",11,'bold')).grid(row=4,column=1,padx=15,pady=15)
Button3=Button(frame2,command=fun3,text="New Route",bg="SlateBlue4",font=("Montserrat",11,'bold')).grid(row=4,column=2,padx=15,pady=15)
Button4=Button(frame2,text="New Run",command=fun4,bg="orchid1",font=("Montserrat",11,'bold')).grid(row=4,column=3,padx=15,pady=15)
