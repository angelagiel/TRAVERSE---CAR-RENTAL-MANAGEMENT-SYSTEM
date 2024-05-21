from tkinter import *
from tkinter import messagebox
import tkinter as tk 
import database_handler
from tkinter import ttk
import models
import random
from database_handler import DBHandler
import re 
from datetime import datetime, timedelta
from PIL import Image, ImageTk

class BillingPage(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
        #----- TRAVERSE LOGO
        logo = Image.open("3traverse logo.png")
        logo = logo.resize((200, 200))
        self.logo = ImageTk.PhotoImage(logo)
        
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, sticky='w', padx=(250, 0))
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Billing Information', fg='#4caf50', font=('Roboto', 40, 'bold'), bg='white')
        self.heading.grid(row=0, column=0, columnspan=5, pady=(0, 0), padx=(450, 0), sticky='w')
        
        #----- CUSTOMER FRAME FIELDS
        self.customer_frame = tk.Frame(self, width=600, border=5 )
        self.customer_frame.grid(row=1, column=0, sticky='nw', pady=(0,0), padx=(100,0))
        
        tk.Label(self.customer_frame, text="Customer ID:", bg='white').grid(row=0, column=0, sticky='w')
        self.customer_id_entry = Entry(self.customer_frame, width=40)
        self.customer_id_entry.grid(row=0, column=1)
        
        tk.Label(self.customer_frame, text="Customer Name:", bg='white').grid(row=1, column=0, sticky='w')
        self.customer_name_entry = Entry(self.customer_frame, width=40)
        self.customer_name_entry.grid(row=1, column=1)
        
        tk.Label(self.customer_frame, text="Driver's License Number:", bg='white').grid(row=2, column=0, sticky='w')
        self.license_number_entry = Entry(self.customer_frame, width=40)
        self.license_number_entry.grid(row=2, column=1)
        
        tk.Label(self.customer_frame, text="Contact Number:", bg='white').grid(row=3, column=0, sticky='w')
        self.contact_number_entry = Entry(self.customer_frame, width=40)
        self.contact_number_entry.grid(row=3, column=1)
        
        #----- CAR FRAME FIELDS
        
        self.car_frame = tk.Frame(self,border=5)
        self.car_frame.grid(row=1, column=0, sticky='nw', pady=(100,0))
        self.car_frame.config(bg='white')
        
        car = Image.open("toyota.png")
        car = car.resize((350, 120))
        self.car = ImageTk.PhotoImage(car)
        
        tk.Label(self.car_frame, image=self.car, bg='white').grid(row=3, column=0, padx=(100, 0))
        
        tk.Label(self.car_frame, text='Selected Car Information',fg='#4caf50', font=('Roboto', 15, 'bold')).grid(row=0, column=0, sticky='w',padx=(100,0))
        
        tk.Label(self.car_frame, text="Car ID:", bg='white').grid(row=1, column=2, sticky='w')
        self.car_id_entry = Entry(self.car_frame, width=25)
        self.car_id_entry.grid(row=1, column=3)
        
        tk.Label(self.car_frame, text="Brand:", bg='white').grid(row=2, column=2, sticky='w')
        self.car_brand_entry = Entry(self.car_frame, width=25)
        self.car_brand_entry.grid(row=2, column=3)
        
        tk.Label(self.car_frame, text="Model:", bg='white').grid(row=3, column=2, sticky='w')
        self.car_model_entry = Entry(self.car_frame, width=25)
        self.car_model_entry.grid(row=3, column=3)
        
        tk.Label(self.car_frame, text="Plate Number:", bg='white').grid(row=4, column=2, sticky='w')
        self.plate_number_entry = Entry(self.car_frame, width=25)
        self.plate_number_entry.grid(row=4, column=3)
        
        tk.Label(self.car_frame, text="Fuel Type:", bg='white').grid(row=5, column=2, sticky='w')
        self.fuel_type_entry = Entry(self.car_frame, width=25)
        self.fuel_type_entry.grid(row=5, column=3)
        
        tk.Label(self.car_frame, text="Seating Capacity:", bg='white').grid(row=6, column=2, sticky='w')
        self.seating_capacity_entry = Entry(self.car_frame, width=25)
        self.seating_capacity_entry.grid(row=6, column=3)
        
        tk.Label(self.car_frame, text="Pickup Location:", bg='white').grid(row=7, column=2, sticky='w')
        self.location_entry = Entry(self.car_frame, width=25)
        self.location_entry.grid(row=7, column=3)
        
        tk.Label(self.car_frame, text="Cost Per Day:", bg='white').grid(row=8, column=2, sticky='w')
        self.cost_per_day_entry = Entry(self.car_frame, width=25)
        self.cost_per_day_entry.grid(row=8, column=3)
        
        tk.Label(self.car_frame, text="Rental Period (days):", bg='white').grid(row=9, column=2, sticky='w')
        self.rental_period_entry = Entry(self.car_frame, width=25)
        self.rental_period_entry.grid(row=9, column=3)
        
        self.confirm_rent = Button(self.car_frame, text='Confirm Rent', pady=2, padx=7, bg='#4caf50', fg='white', width=25, command=self.confirm_rent_clicked)
        self.confirm_rent.grid(row=10, column=3, pady=(20,0), padx=(10, 60))
        
        tk.Button(self.car_frame, text="Logout", pady=2, padx=7, bg='#4caf50', fg='white', width=14,  command=self.go_to_login_page).grid(row=10, column=2, pady=(20,0), padx=(0, 0))

        
        #----- BILLING FRAME FIELDS
        
        self.billing_frame = tk.Frame(self, width=600, height=400, border=1, highlightthickness=2, highlightbackground="#000", highlightcolor="#000", bd=0)
        self.billing_frame.grid(row=1, column=2, columnspan=4)
        # self.billing_frame.config(bg='white')
        
        tk.Label(self.billing_frame, text="Billing Receipt", fg='black', font=('Roboto', 15, 'bold')).grid(row=0, column=0, padx=(10,0))
        
        tk.Label(self.billing_frame, text="Customer Name:").grid(row=1, column=0, sticky='w', padx=10, pady=10)
        self.customer_name_entry_billing = Entry(self.billing_frame)
        self.customer_name_entry_billing.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Rented Model:").grid(row=2, column=0, sticky='w', padx=10, pady=10)
        self.rented_model_entry_billing = Entry(self.billing_frame)
        self.rented_model_entry_billing.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Rented Date-Time:").grid(row=3, column=0, sticky='w', padx=10, pady=10)
        self.rented_date_entry_billing = Entry(self.billing_frame)
        self.rented_date_entry_billing.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Rental Period:").grid(row=4, column=0, sticky='w', padx=10, pady=10)
        self.rental_period_entry_billing = Entry(self.billing_frame)
        self.rental_period_entry_billing.grid(row=4, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Return Date-Time:").grid(row=5, column=0, sticky='w', padx=10, pady=10)
        self.return_date_entry_billing = Entry(self.billing_frame)
        self.return_date_entry_billing.grid(row=5, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Pickup Location:").grid(row=6, column=0, sticky='w', padx=10, pady=10)
        self.pickup_location_entry_billing = Entry(self.billing_frame)
        self.pickup_location_entry_billing.grid(row=6, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Cost Per Day:").grid(row=7, column=0, sticky='w', padx=10, pady=10)
        self.cost_per_day_billing_entry = Entry(self.billing_frame)
        self.cost_per_day_billing_entry.grid(row=7, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="================================:").grid(row=8, column=0, columnspan=2, sticky='w', padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Total Rent:").grid(row=9, column=0, sticky='w', padx=10, pady=10)
        self.total_rent_entry = Entry(self.billing_frame)
        self.total_rent_entry.grid(row=9, column=1, padx=10, pady=10)
        
        
        

    def on_return(self, **kwargs):
        print("Received kwargs:", kwargs)
        self.customer_id_entry.delete(0, tk.END)
        self.car_id_entry.delete(0, tk.END)
        
        customer_id = kwargs.get('customer_id')
        car_id = kwargs.get('car_id')
        
        if not car_id:
            print("Error: 'car_id' not found in kwargs")
            return
        
        db_conn = database_handler.DBHandler()
        customer_data = db_conn.read_one_customer(customer_id)
        car_data = db_conn.read_one_car(car_id)
        db_conn.close()
        
        self.clear_fields()
        
        if customer_data:
            self.customer_id_entry.insert(0, customer_data.id)
            self.customer_name_entry.insert(0, customer_data.name)
            self.license_number_entry.insert(0, customer_data.license_number)
            self.contact_number_entry.insert(0, customer_data.contact)
        
        if car_data:
            self.car_id_entry.insert(0, car_data.id)
            self.car_brand_entry.insert(0, car_data.brand)
            self.car_model_entry.insert(0, car_data.model)
            self.plate_number_entry.insert(0, car_data.plate_number)
            self.fuel_type_entry.insert(0, car_data.fuel_type)
            self.seating_capacity_entry.insert(0, car_data.seating_capacity)
            self.location_entry.insert(0, car_data.location)
            self.cost_per_day_entry.insert(0, car_data.cost_per_day)

    def clear_fields(self): 
        self.customer_id_entry.delete(0, tk.END)
        self.customer_name_entry.delete(0, tk.END)
        self.license_number_entry.delete(0, tk.END)
        self.contact_number_entry.delete(0, tk.END)

        self.car_id_entry.delete(0, tk.END)
        self.car_brand_entry.delete(0, tk.END)
        self.car_model_entry.delete(0, tk.END)
        self.plate_number_entry.delete(0, tk.END)
        self.fuel_type_entry.delete(0, tk.END)
        self.seating_capacity_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.cost_per_day_entry.delete(0, tk.END)

    def clear_billing_fields(self): 
        
        self.customer_name_entry_billing.delete(0, tk.END)
        self.rented_model_entry_billing.delete(0, tk.END)
        self.rented_date_entry_billing.delete(0, tk.END)
        self.rental_period_entry_billing.delete(0, tk.END)
        self.return_date_entry_billing.delete(0, tk.END)
        self.pickup_location_entry_billing.delete(0, tk.END)
        self.cost_per_day_billing_entry.delete(0, tk.END)
        self.total_rent_entry.delete(0, tk.END)
        
        
        
        
    def confirm_rent_clicked(self):
        current_datetime = datetime.now()
        rental_period = int(self.rental_period_entry.get())
        cost_per_day = float(self.cost_per_day_entry.get())  

        new_rental = models.Rental()
        new_rental.customer_id = self.customer_id_entry.get()
        new_rental.customer_name = self.customer_name_entry.get()  
        new_rental.car_id = self.car_id_entry.get()
        new_rental.rental_status = "UNAVAILABLE"
        new_rental.rented_model = self.car_model_entry.get()
        new_rental.rent_plateNo = self.plate_number_entry.get()
        new_rental.rental_period = rental_period
        new_rental.rent_datetime = current_datetime  # Store datetime object directly

        # Calculate return datetime
        return_datetime = current_datetime + timedelta(days=rental_period)

        new_rental.return_datetime = return_datetime  # Store datetime object directly

        new_rental.pickup_location = self.location_entry.get()
        new_rental.cost_per_day = cost_per_day
        new_rental.total_rent = cost_per_day * rental_period

        db_conn = database_handler.DBHandler()
        db_conn.add_rental(new_rental)
        db_conn.close()
        
        self.clear_billing_fields()
        
        self.customer_name_entry_billing.insert(0, new_rental.customer_name)
        self.rented_model_entry_billing.insert(0, new_rental.rented_model)
        self.rented_date_entry_billing.insert(0, new_rental.rent_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        self.rental_period_entry_billing.insert(0, new_rental.rental_period)
        self.return_date_entry_billing.insert(0, new_rental.return_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        self.pickup_location_entry_billing.insert(0, new_rental.pickup_location)
        self.cost_per_day_billing_entry.insert(0, new_rental.cost_per_day)
        self.total_rent_entry.insert(0, new_rental.total_rent)

        self.confirm_rent.focus_set()

        
    def go_to_login_page(self): 
        self.parent.change_window('Login_Page')