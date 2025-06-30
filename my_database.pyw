import sqlite3
from tkinter import messagebox
def connect_database():
    con=sqlite3.Connection("Your_database.db")
    return con


con=connect_database()
cur=con.cursor()

cur.execute('''
create table if not exists operator(
    Operator_Id text primary key,
    Name varchar(20),
    Address varchar(30),
    Phone  int,
    Email varchar(30)
)
''')

cur.execute('''
create table if not exists bus(
    Bus_Id text primary key,
    Type text,
    Capacity int,
    Fare int,
    Operator_Id text references operator(Operator_Id) on delete cascade on update cascade,
    Route_Id text references route(Route_Id) on delete cascade on update cascade
)
''')

cur.execute('''
create table if not exists route(
    Route_Id text,
    Station_Name text,
    Station_Id text,
    primary key (Route_Id,Station_Name) 
)
''')


cur.execute('''
CREATE TABLE IF NOT EXISTS run (
    Bus_Id text ,
    Running_Date text,
    Seat_Available int,
    PRIMARY KEY (Bus_Id, Running_Date),
    FOREIGN KEY (Bus_Id) REFERENCES bus(Bus_Id) ON DELETE CASCADE ON UPDATE CASCADE
)
''')



cur.execute('''
create table if not exists Booking_Details(
    Ref_no text Primary key,
    Start_Station_Id text ,
    End_Station_Id text ,
    Booking_Date text,
    Travel_Date text,
    Name text,
    Gender text,
    Total_Seat int,
    Mobile_No int,
    Age int,
    Bus_Id text references bus(Bus_Id)     
)
''')


    

    
