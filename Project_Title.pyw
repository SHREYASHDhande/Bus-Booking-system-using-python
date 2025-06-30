from tkinter import *
root1=Tk()
root1.title("Title")
root1.geometry('800x700')
my_image=PhotoImage(file="starbusx.png")
L1=Label(image=my_image).pack()
def fun(event):
    root1.destroy()
    import Project_HomePage
    
    
L2=Label(root1,text="Welcome to Online Bus Booking system ",pady=15,bd=1,font=("ARIAL",28,"bold"),bg="WHITE").pack()
L3=Label(root1,text="Name:MANAN JAIN",pady=10,fg="DeepSkyBlue4",font=("ARIAL",12)).pack()
L4=Label(root1,text="Enrollment:221B501",pady=10,fg="DeepSkyBlue4",font=("ARIAL",12)).pack()
L5=Label(root1,text="Mobile:9587207803",pady=10,fg="DeepSkyBlue4",font=("ARIAL",12)).pack()
L6=Label(root1,text="Submitted to:Dr.Mahesh Kumar",pady=10,fg="DeepSkyBlue4",font=("ARIAL",20)).pack()
L7=Label(root1,text="Project Based Learning",fg="Red",font=("ARIAL",10)).pack()
status=Label(root1,text="Press any key to continue!",bd=1,font=("ARIAL",10),relief=SUNKEN,anchor=E).pack()
root1.bind("<KeyPress>",fun)
root1.mainloop() 

