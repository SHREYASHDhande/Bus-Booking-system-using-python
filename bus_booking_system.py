import sqlite3
from tkinter import messagebox
import my_database as use

    
def add_booking_details(passenger_data):
    conn = use.connect_database()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO  Booking_Details (Ref_no,Start_Station_Id, End_Station_Id, Booking_Date, 
        Travel_Date,Name,Gender,Total_Seat,Mobile_No ,Age,Bus_Id)
        VALUES (?, ?, ?, ?,?,?,?,?,?,?,?)
    ''', passenger_data)

    conn.commit()
    conn.close()
    

def add_operator(operator_data):
    conn = use.connect_database()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO operator (Operator_Id, Name, Address, Phone, Email)
        VALUES (?, ?, ?, ?, ?)
    ''', operator_data)

    conn.commit()
    conn.close()


def edit_operator(op_id,operator_data):
    conn = use.connect_database()
    cursor = conn.cursor()

    cursor.execute('''
        update operator set Operator_Id=?, Name=?, Address=?, Phone=?, Email=?
        where Operator_Id=?
    ''',(*operator_data,op_id) )

    conn.commit()
    conn.close()


def add_bus(bus_data):
    conn = use.connect_database()
    cursor = conn.cursor()

    try:
        cursor.execute('select * from route where Route_Id = ?', (bus_data[5],))
        if not cursor.fetchone():
            messagebox.showerror("Error", "Route_id does not exist.")
            conn.rollback()
            return

        cursor.execute('SELECT * FROM operator WHERE Operator_Id = ?', (bus_data[4],))
        if not cursor.fetchone():
            messagebox.showerror("Error", "Operator_id does not exist.")
            conn.rollback()
            return

        cursor.execute('''
            INSERT INTO bus (
                Bus_Id,
                Type,
                Capacity,
                Fare,
                Operator_Id,
                Route_Id
            )
            VALUES (?, ?, ?, ?, ?, ?)
        ''', bus_data)

        conn.commit()
        return 1
    except Exception as e:
        #messagebox.showerror("Error", f"Error adding bus: {e}")
        conn.rollback()
        return
    finally:
        conn.close()


def edit_bus(busid,bus_data):
    conn = use.connect_database()
    cursor = conn.cursor()

    cursor.execute('select * from route where Route_Id = ?',(bus_data[5],))
    if not cursor.fetchone():
        messagebox.showerror("Error","Route_Id does not exist.")
        conn.rollback()
        return 

    cursor.execute('SELECT * FROM operator WHERE Operator_Id = ?', (bus_data[4],))
    if not cursor.fetchone():
        messagebox.showerror("Error","Operator_Id does not exist.")
        conn.rollback()
        return

    cursor.execute('''
        update bus set
         Bus_Id=?,
         Type=?,
          Capacity=?, 
          Fare=?, 
          Operator_Id=?,
          Route_Id=?
        where Bus_Id=?
    ''',(*bus_data,busid) )

    conn.commit()
    conn.close()

from tkinter import messagebox

def add_route(route_data):
    conn = use.connect_database()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO route  (
               Route_Id, Station_Name, Station_Id)
            VALUES (?, ?, ?)
        ''', route_data)

        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        messagebox.showerror("Error", f"Failed to add route: {e}")
        return


def add_newrun(newrun_data):
    conn = use.connect_database()
    cursor = conn.cursor()

    try:
        # Check if the record already exists
        cursor.execute('SELECT * FROM run WHERE Bus_Id = ? AND Running_Date = ?', (newrun_data[0], newrun_data[1]))
        if cursor.fetchone():
            messagebox.showerror("Error", "Record already exists.")
            return

        # Insert the new record
        cursor.execute('''
            INSERT INTO run (
               Bus_Id,
               Running_Date,
               Seat_Available
            )
            VALUES (?, ?, ?)
        ''', newrun_data)

        conn.commit()
    except Exception as e:
        messagebox.showerror("Error", f"Error adding new_run record: {e}")
        conn.rollback()
    finally:
        conn.close()




def delete_route(route_id, station):
    conn = use.connect_database()
    cursor = conn.cursor()

    # Use a parameterized query for composite primary key
    cursor.execute('DELETE FROM route WHERE Route_Id = ? AND Station_Name = ?', (route_id, station))

    conn.commit()
    conn.close()



def delete_newrun(bus_id, running_date):
    conn = use.connect_database()
    cursor = conn.cursor()

    try:
        # Use parameterized query to avoid SQL injection
        cursor.execute('DELETE FROM run WHERE Bus_Id = ? AND Running_Date = ?', (bus_id, running_date))

        # Check if any rows were affected
        if cursor.rowcount == 0:
            messagebox.showerror("Error", "Record not found.")
        conn.commit()
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting new_run record: {e}")
        conn.rollback()
    finally:
        conn.close()



def read_operators():
    conn = use.connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM operator')
    operators = cursor.fetchall()

    conn.close()

    return operators

print("\n operator  data:\n")
print(read_operators())


def read_bus():
    conn = use.connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM bus')
    operators = cursor.fetchall()

    conn.close()

    return operators

print("\nBus data:\n")
print(read_bus())


def read_route():
    conn = use.connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM route')
    
    operators = cursor.fetchall()

    conn.close()

    return operators

print("\nroute data:\n")
print(read_route())

def read_booking():
    conn = use.connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Booking_Details')
    
    operators = cursor.fetchall()

    conn.close()

    return operators

print("\nbooking data:\n")
print(read_booking())


def ticket(refer_no):
    conn = use.connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Booking_Details where Ref_no=? ',(refer_no,))
    
    operators = cursor.fetchall()

    conn.close()

    return operators


def show_tickets_from_mobile(mobile_no):
    conn = use.connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Booking_Details where Mobile_No =? ',(mobile_no,))
    
    operators = cursor.fetchall()

    conn.close()

    return operators
def read_newrun():
    conn = use.connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM run')
    operators = cursor.fetchall()

    conn.close()

    return operators

print("\nnew run data:\n")
print(read_newrun())


def show_route(start_station_name, end_station_name):
    conn = use.connect_database()
    cursor = conn.cursor()

    # Use a self-join to find route_ids that have both start and end stations
    cur = cursor.execute('''
        SELECT r1.Route_Id
        FROM route r1
        JOIN route r2 ON r1.Route_Id = r2.Route_Id
        WHERE r1.Station_Name = ? AND r2.Station_Name = ?
    ''', (start_station_name, end_station_name))

    route = cur.fetchall()

    conn.close()
    return route



def show_bus(route):
    conn = use.connect_database()
    cursor = conn.cursor()

    
    cur = cursor.execute('''
        select Bus_Id from bus where Route_Id =?
    ''', (route))

    buses = cur.fetchall()

    conn.close()
    return buses

def show_bus_fare(bus_id):
    conn = use.connect_database()
    cursor = conn.cursor()

    
    cur = cursor.execute('''
        select Fare from bus where Bus_Id =?
    ''', (bus_id,))

    buses = cur.fetchone()

    conn.close()
    return buses

def show_run(bus_id,Journey_date):
    conn = use.connect_database()
    cursor = conn.cursor()

    
    cur = cursor.execute('''
        select Bus_Id from run where Bus_Id =? and Running_Date=?''',(bus_id,Journey_date))

    buses = cur.fetchall()

    conn.close()
    return buses


def show_operator(bus_id):
    conn = use.connect_database()
    cursor = conn.cursor()

    # Use a join operation to get the operator details associated with the bus_id
    cur = cursor.execute('''
        SELECT bo.Name
        FROM bus bd
        JOIN operator bo ON bd.Operator_Id = bo.Operator_Id
        WHERE bd.Bus_Id = ?
    ''', (bus_id,))

    operator_name = cur.fetchone()

    conn.close()
    return operator_name


def show_bus_type(busid):
    conn = use.connect_database()
    cursor = conn.cursor()

    cur=cursor.execute('select Type from bus where Bus_Id=?',(busid,))
    bus_type=cur.fetchone()

   
    conn.close()
    return bus_type



def show_avail(bus_id, running_date):
    conn = use.connect_database()
    cursor = conn.cursor()

    try:
        # Use a parameterized query to avoid SQL injection
        cursor.execute('SELECT Seat_Available FROM run WHERE Bus_Id = ? AND Running_Date = ?', (bus_id, running_date))
        seat = cursor.fetchone()

        return seat[0] if seat else None
    except Exception as e:
        print(f"Error in show_avail: {e}")
        return None
    finally:
        conn.close()



def edit_avail(bus_id, total_seat, Journey_date):
    conn = use.connect_database()
    cursor = conn.cursor()

    try:
        # Use a parameterized query to avoid SQL injection
        cursor.execute('SELECT Seat_Available FROM run WHERE Bus_Id = ? AND Running_Date = ?', (bus_id, Journey_date))
        seat = cursor.fetchone()

        if seat:
            remaining_seats = int(seat[0]) - int(total_seat)

            # Update the available seats in the new_run table
            cursor.execute('UPDATE run SET Seat_Available=? WHERE Bus_Id=? AND Running_Date=?', (remaining_seats, bus_id, Journey_date))
            conn.commit()
        else:
            print("Record not found for the specified Bus_Id and Running_Date.")
    except Exception as e:
        print(f"Error in edit_avail: {e}")
        conn.rollback()
    finally:
        conn.close()

def show_cap(busid):
    conn = use.connect_database()
    cursor = conn.cursor()

    cur=cursor.execute('select Capacity from bus where Bus_Id=?',(busid,))
    bus_type=cur.fetchone()

    conn.close()
    return bus_type


def show_fare(busid):
    conn = use.connect_database()
    cursor = conn.cursor()

    cur=cursor.execute('select Fare from bus where Bus_Id=?',(busid,))
    bus_fare=cur.fetchone()

    conn.commit()
    conn.close()
    return bus_fare

print(show_operator("1"))
