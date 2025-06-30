from tkinter import *
from tkinter import messagebox
from datetime import datetime
import my_database as use
import random
import bus_booking_system
root=Tk()
root.title("Bus Book")
root.geometry('1200x900')
current_date=datetime.now().strftime("%d/%m/%Y")

def home_window():
    root.destroy()
    import Project_HomePage
def generate_booking_reference():
    while True:
        reference_number = random.randint(1, 100)  
        existing_bookings=bus_booking_system.read_booking()
        booking_edit=None
        for op in existing_bookings:
            if op[0]==reference_number:
                booking_edit=op[0]
                break
        if reference_number != booking_edit:
            return reference_number
selected_bus = StringVar()
selected_bus.set("None")

def passenger_data():
    
    name = name_entry.get()
    gender = click.get()
    global total_seat
    total_seat = seat_entry.get()
    mobile_no = mobile_entry.get()
    age = age_entry.get()
    bus_id = selected_bus.get()
    
    available = bus_booking_system.show_avail(bus_id,Journey_date)
    
        
    if (not ( name and gender and total_seat and mobile_no and age)):
            messagebox.showwarning("Warning", "All entries should be filled.")
            return
    if total_seat.isalpha ==True:
        messagebox.showerror("error", "Enter correct seats")
        return
    if int(total_seat)>int(available):
        messagebox.showerror("error", "total_seats  are greater than availabilty")
        return
    
    if(name.isdigit()):
        messagebox.showwarning("Warning", " Name should  be Alphabatical .")
        return
        
    if(click.get()=="Select"):
        messagebox.showwarning("Warning", " Gender Should Be Selected .")
        return
        
    #check if mobile no is integer and of 10 digits
    if not ((len(mobile_no)==10)and mobile_no.isdigit()) :
                messagebox.showerror("Error","Mobile No. should be Ten digit Integer. ")
                return
    if  (age.isalpha()) :
        messagebox.showerror("error"," Age Should be Integer ")
        return
            
    if int(age)>110 :
        messagebox.showerror("error"," Age Should be less than 110")
        return

    if int(age)<18 :
        messagebox.showerror("error"," Age Should be aleast 18")
        return
    
    if not(total_seat.isdigit()) :
        messagebox.showerror("error"," seat should be Integer")
        return 
    if(int(total_seat)>7) :
        messagebox.showerror("error"," max seat 6 seat can be booked")
        return
    if(int(total_seat)<=0) :
        messagebox.showerror("error"," min seat 1 seat can be booked")
        return
        

    
    bus_fare=bus_booking_system.show_fare(bus_id)            
    total_fare=(int(total_seat)*int(bus_fare[0]))

   

    data=generate_booking_reference(), start_station, end_station, current_date, Journey_date,name, gender, total_seat, mobile_no, age, bus_id

    response=messagebox.askyesno("Seat Confirm",f'''Total amount to be paid is {total_fare} /Do you want to Book? ''')
    if response==1:
            messagebox.showinfo("congrats", "your bus booked successfully")
           
            bus_booking_system.add_booking_details(data)
            bus_booking_system.edit_avail(bus_id,total_seat,Journey_date)
            root.destroy()
            import Project_ticket
                        
    else:

        return


def book_bus():

    

    
    if(selected_bus.get()=="None"):

        
        messagebox.showerror("error","bus is not selected ")
        return
    
        


    Label(frame3, text="Fill Passenger details to book the Bus ticket", fg="red", relief="ridge", bg="cyan3",
          font=('ARIAL,12')).grid(row=0, column=1, padx=10, pady=20, columnspan=10)

    
    Label(frame3, text="Full Name : ", font=('ARIAL,9')).grid(row=1, column=0)
    global name_entry
    name_entry = Entry(frame3)
    name_entry.grid(row=1, column=1)

    Label(frame3, text="Gender : ", font=('ARIAL,9')).grid(row=1, column=2)
    gender_options = ["Male", "Female", "Other"]
    global click
    click = StringVar()
    click.set("Select")
    OptionMenu(frame3, click, *gender_options).grid(row=1, column=3)


    Label(frame3, text="Total Seats: ", font=('ARIAL,9')).grid(row=1, column=4)
    global seat_entry
    seat_entry = Entry(frame3)
    seat_entry.grid(row=1, column=5)


    Label(frame3, text="Mobile no. : ", font=('ARIAL,9')).grid(row=1, column=6)
    global mobile_entry
    mobile_entry = Entry(frame3)
    mobile_entry.grid(row=1, column=7)

    Label(frame3, text="Age : ", font=('ARIAL,9')).grid(row=1, column=8)
    global age_entry
    age_entry = Entry(frame3)
    age_entry.grid(row=1, column=9, padx=10)


    Button(frame3, text="Book Seat", fg="red", bg="cyan3", font=('ARIAL,9'),command=passenger_data).grid(row=10, column=5)

def display_buses(buses_running):
    k = 6
    l = 1

    def on_radio_click(bus_id):
        selected_bus.set(bus_id)
        

    for i in range(len(buses_running)):
        bus_id = buses_running[i]
        available = bus_booking_system.show_avail(bus_id,Journey_date)

        
        if int(available)>0:
            
            
        
            Radiobutton(frame2, text=f'Bus {i + 1}', bg="yellow", font=('ARIAL,10'),
                        relief="ridge", variable=selected_bus, value=bus_id, command=lambda bus_id=bus_id: on_radio_click(bus_id)).grid(row=k,column=l,pady=10,padx=10)
            operator_name = bus_booking_system.show_operator(bus_id)
            l = l + 1
            Label(frame2, text=operator_name[0], fg="blue", font=('ARIAL,10')).grid(row=k, column=l, padx=10)
            bus_type = bus_booking_system.show_bus_type(bus_id)
            l = l + 1
            Label(frame2, text=bus_type[0], fg="blue", font=('ARIAL,10')).grid(row=k, column=l, padx=10)
            available = bus_booking_system.show_avail(bus_id,Journey_date)
            cap = bus_booking_system.show_cap(bus_id)
            l = l + 1
            Label(frame2, text=f'{available}/{cap[0]}', fg="blue", font=('ARIAL,10')).grid(row=k, column=l,
                                                                                                           padx=10)
            l = l + 1
            fare = bus_booking_system.show_fare(bus_id)
            Label(frame2, text=fare[0], fg="blue", font=('ARIAL,10')).grid(row=k, column=l, padx=10)
            k = k + 1
            l = 1
    

    Button(frame2, text="Proceed to Book", bg="red", font=('ARIAL,6'), command=book_bus,width=15).grid(row=k-1, column=6)


def show_bus():

    global start_station
    global end_station
    global Journey_date

    start_station=start.get()
    end_station=end.get()
    Journey_date=date.get()
    

    if not (start_station and end_station and Journey_date ):
        messagebox.showwarning("Warning","All entries should be filled.")
        return
    try:
        
        datetime.strptime(Journey_date, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use dd/mm/yyyy.")
        return
    

    if start_station.isalpha() and end_station.isalpha():
        #if journey date in not empty
        if not Journey_date=="":
            

            start_station=start_station.capitalize()
            end_station=end_station.capitalize()
            route = bus_booking_system.show_route(start_station,end_station)

            if len(route)==0:
                messagebox.showerror("No route found","No route found")
                return
            else:

                buses=bus_booking_system.show_bus(route[0])
                
            if(len(buses)==0):
                messagebox.showerror("No Bus found","No Bus found")
                return

            else:
                buses_running=[]
                for i in buses:
                    if(i in bus_booking_system.show_run(i[0],Journey_date)):
                        buses_running.append(i[0])
                if(len(buses_running)==0):
                        messagebox.showerror("NOT RUNNING",f'BUS is not running at {Journey_date} , Change Date ')
                        return
    
    Label(frame2,text="Select Bus",fg="Black",font=('ARIAL')).grid(row=5,column=1,padx=10)
    
    Label(frame2,text="Operator",fg="Black",font=('ARIAL')).grid(row=5,column=2,padx=10)
    
    Label(frame2,text="Bus Type",fg="Black",font=('ARIAL')).grid(row=5,column=3,padx=10)

    Label(frame2,text="Available/Capacity",fg="Black",font=('ARIAL')).grid(row=5,column=4,padx=10)

    Label(frame2,text="Fare",fg="Black",font=('ARIAL')).grid(row=5,column=5,padx=10)
    

    display_buses(buses_running)
    
    start.delete(0,END)
    end.delete(0,END)
    date.delete(0,END)
  



my_image=PhotoImage(file="starbusx.png")
my_button_img=PhotoImage(file="Button.png")
my_label=Label(image=my_button_img)
frame1=Frame(root,padx=10,pady=10,bd=1)
frame1.pack()
L1=Label(frame1,image=my_image,pady=15).grid(row=1,column=2)
L2=Label(frame1,text=" Online Bus Booking system ",pady=15,bd=1,font=("ARIAL",14),bg="gold").grid(row=2,column=2)

frame=Frame(root,padx=10,pady=10,bd=1)
frame.pack()
L3=Label(frame,text=" Enter Journey Details ",bd=3,font=("ARIAL",12),bg="gold").grid(row=3,column=2)



frame2=Frame(root)
frame2.pack(pady=30)
Label1=Label(frame2,text="From",font=("ARIAL",9)).grid(row=4,column=0)
start=Entry(frame2)
start.grid(row=4,column=1,padx=10)
Label2=Label(frame2,text="to",font=("ARIAL",9)).grid(row=4,column=2)
end=Entry(frame2)
end.grid(row=4,column=3,padx=10)
Label3=Label(frame2,text="Journey Date",font=("ARIAL",9)).grid(row=4,column=4)
date=Entry(frame2)


date.grid(row=4,column=5,padx=10)

frame3=LabelFrame(root,borderwidth=0)
frame3.pack()

Button1=Button(frame2,text="Show Bus",bg="bisque",font=("ARIAL",9,'bold'),command=show_bus).grid(row=4,column=6,padx=10)
Button2=Button(frame2,bg="SeaGreen1",image=my_button_img,command=home_window).grid(row=4,column=7,padx=10)




