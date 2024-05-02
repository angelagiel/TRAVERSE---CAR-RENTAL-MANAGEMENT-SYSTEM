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

class CustomerWindow(tk.Frame): 
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
        self.heading = tk.Label(self, text='Hello, Customer!', fg='#4caf50', font=('Roboto', 40, 'bold'), bg='white')
        self.heading.grid(row=1, column=0, padx=(150,100), pady=(0, 50), sticky='n')
        
        #------ CUSTOMER FIELDS 
        self.customer_id = tk.Label(self, text='Customer ID:', fg='#4caf50', font=('Inter', 18, 'bold'), bg='white')
        self.customer_id.grid(row=2, column=0, sticky='w', padx=(100, 100), pady=(0,0))
        self.id_num = tk.Label(self, text='6', fg='black', font=('Inter', 12), bg='white' )
        self.id_num.grid(row=2, column=0, sticky='w', padx=(300,0))
        
        self.customer_name = tk.Label(self, text='Customer Name:', fg='#4caf50', font=('Inter', 18, 'bold'), bg='white')
        self.customer_name.grid(row=3, column=0, sticky='wn', padx=(100,100), pady=(0,0))
        self.name_customer = tk.Label(self, text='Elon Musk', fg='black', font=('Inter', 12), bg='white' )
        self.name_customer.grid(row=3, column=0, sticky='wn', padx=(300,0))
        
        
        #----- SEARCH FIELD
        
        tk.Label(self, text="Search by Brand: ", font=('Inter', 13), bg='white').grid(row=3, column=0, sticky='w', pady=(70,0), padx=(100,0))
        
        self.search_field = tk.Entry(self, width=140)
        self.search_field.grid(row=3, column=0, pady=(70, 0), padx=(120, 0))
        self.search_field.bind('<KeyRelease>', self.update_table)
        
        #----- TABLE 
        columns = ('id', 'brand', 'model', 'plate#', 'fuel', 'cost', 'seating capacity', 'location', 'availability')
        
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
        self.table.heading('availability', text='Status')
        
        self.table.grid(row=4, column=0, padx=(100, 100))

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
        self.table.column('availability', width=145)
        # self.table.tag_configure("center", anchor="center")
        self.update_table()
        
        #------ Logout BUTTON
        self.menu_button = tk.Button(self, text='Menu', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.go_to_login_page)
        self.menu_button.grid(row=5, column=0, padx=(300,0), sticky='w',pady=(20,0))
        
        #------ View Profile
        self.delete_button = tk.Button(self, text='Delete', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'))
        self.delete_button.grid(row=5, column=0, padx=(400, 100), pady=(20,0))
        #-----  Billing Page
        self.rent_car = tk.Button(self, text='RENT CAR', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.go_to_billing_page)
        self.rent_car.grid(row=5, column=0, padx=(60, 100), pady=(20,0))
        
    def update_table(self, event=None):
        # pass
        self.get_car_list()

        self.table.delete(*self.table.get_children())
        #----- TRIAL
        # logo = Image.open("250traverse logo.png")
        # logo = logo.resize((150, 150))
        # self.logo = ImageTk.PhotoImage(logo)
        
        for car in self.car_list:
            if car.availability != 1:
                car.availabilty = 'Not Available'
            else: 
                car.availability = 'Available'
                
            row = (car.id, car.brand, car.model, car.plate_number, car.fuel_type, car.cost_per_day, car.seating_capacity, car.location, car.availability)
            self.table.insert('', tk.END, values=row)   


    def get_car_list(self):
        # pass
        key = self.search_field.get()
        db_conn = database_handler.DBHandler()
        self.car_list = db_conn.search_car(key)
        db_conn.close()
    
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
        

        
    def go_to_car_page(self): 
        selected_items = self.table.selection()
        if len(selected_items) == 0:
            messagebox.showwarning("Update Car", "Select a car to update.")
            return

        for item in selected_items:
            id = self.table.item(item)['values'][0]
            self.parent.change_window('View_Car', car_id=id)

    #----
    def go_to_login_page(self): 
        self.parent.change_window('Login_Page')
    
    def go_to_billing_page(self): 
        self.parent.change_window('Billing_Page')
        