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

class FleetPage(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
        #----- TRAVERSE LOGO
        logo = Image.open("250traverse logo.png")
        logo = logo.resize((150, 150))
        self.logo = ImageTk.PhotoImage(logo)
        
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, padx=(100,100))
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Car Fleet Management', fg='#4caf50', font=('Roboto', 40, 'bold'), bg='white')
        self.heading.grid(row=1, column=0, padx=(150,100), pady=(0, 50), sticky='n')
        
        #----- SEARCH FIELD
        
        tk.Label(self, text="Search by Brand: ", font=('Inter', 13), bg='white').grid(row=1, column=0, sticky='w', pady=(70,0), padx=(100,0))
        
        self.search_field = tk.Entry(self, width=140)
        self.search_field.grid(row=1, column=0, pady=(70, 0), padx=(120, 0))
        self.search_field.bind('<KeyRelease>', self.update_table)
        
        #----- TABLE 
        columns = ('id', 'brand', 'model', 'plate#', 'fuel', 'cost', 'seating capacity', 'location', 'status')
        
        self.table = ttk.Treeview(self, columns=columns, show='headings')
        
        self.table.heading('id', text='ID')
        # self.table.heading('img', text='Car Image')
        self.table.heading('brand', text='Brand')
        self.table.heading('model', text='Model')
        self.table.heading('plate#', text='Plate Number')
        self.table.heading('fuel', text='Fuel Type')
        self.table.heading('cost', text='Cost/Day')
        self.table.heading('seating capacity', text='Seaters')
        self.table.heading('location', text='Location')
        self.table.heading('status', text='Status')
        
        self.table.grid(row=2, column=0, padx=(100, 100))

        # Set the width of each column
        self.table.column('id', width=30)
        # self.table.column('img', width=200)
        self.table.column('brand', width=150)
        self.table.column('model', width=100)
        self.table.column('plate#', width=120)
        self.table.column('fuel', width=100)
        self.table.column('cost', width=120)
        self.table.column('seating capacity', width=90)
        self.table.column('location', width=145)
        self.table.column('status', width=145)
        # self.table.tag_configure("center", anchor="center")
        self.update_table()
        
        #------ MENU BUTTON
        self.menu_button = tk.Button(self, text='Menu', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.go_to_admin_dashboard)
        self.menu_button.grid(row=3, column=0, padx=(300,0), sticky='w',pady=(20,0))
        
        #------ DELETE CAR
        self.delete_button = tk.Button(self, text='Delete', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.delete_car)
        self.delete_button.grid(row=3, column=0, padx=(400, 100), pady=(20,0))
        #-----  UPDATE CAR
        self.view_car = tk.Button(self, text='Update', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.go_to_car_page)
        self.view_car.grid(row=3, column=0, padx=(60, 100), pady=(20,0))
        
    def update_table(self, event=None):
        self.get_car_list()
        rental_data = self.get_rental_data()
        
        self.table.delete(*self.table.get_children())

        for car in self.car_list:
            car_data = (car.id, car.brand, car.model, car.plate_number, car.fuel_type, car.cost_per_day, car.seating_capacity, car.location)
            
            if car.id in rental_data: 
                rental_info = rental_data[car.id]
                row = car_data + (rental_info,)
            else: 
                 row = car_data + ('----',)
                
            self.table.insert('', tk.END, values=row)


    def get_car_list(self):
        key = self.search_field.get()
        db_conn = database_handler.DBHandler()
        self.car_list = db_conn.search_car(key)
        
        self.rental_statuses = db_conn.get_rental_statuses()
        db_conn.close()
    
    def get_rental_data(self):
        db_conn = database_handler.DBHandler()
        rentals = db_conn.search_rental()
        db_conn.close()

        rental_data = {}  # Dictionary to store rental data for each customer
        for rental in rentals:
            if rental.car_id not in rental_data:
                if rental.rental_status == "UNAVAILABLE": 
                    rental.rental_status = "CURRENTLY RENTED"
                    rental_data[rental.car_id] = (
                        rental.rental_status

                )
        return rental_data

    
    
    def delete_car(self): 
        selected_items = self.table.selection()

        if len(selected_items) == 0: 
            messagebox.showwarning('Delete a Car', 'Please Select a Car to Delete')
            return
        
        proceed = messagebox.askyesno('Delete a Car', 'Are you sure you want to delete?')
        
        if not proceed: 
            return
        
        for item in selected_items: 
            id = self.table.item(item)['values'][0]

            db_conn = database_handler.DBHandler()
            db_conn.delete_car(id)
            db_conn.close()
            
            self.update_table()
    
    def on_return(self): 
        self.update_table()
        
    def go_to_admin_dashboard(self): 
        self.parent.change_window('Admin_Dashboard')
        
    def go_to_car_page(self): 
        selected_items = self.table.selection()
        if len(selected_items) == 0:
            messagebox.showwarning("Update Car", "Select a car to update.")
            return

        for item in selected_items:
            id = self.table.item(item)['values'][0]
            self.parent.change_window('View_Car', car_id=id)
        
        
        